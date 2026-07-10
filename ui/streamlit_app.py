import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")
API_URL = f"{BACKEND_URL}/chat"

st.set_page_config(page_title="AI Weather Assistant", page_icon="🌤️")

st.title("🌤️ AI Weather Assistant")

# ----------------------------
# SESSION STATE (chat memory)
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# DISPLAY CHAT HISTORY
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ----------------------------
# USER INPUT
# ----------------------------
user_input = st.chat_input("Ask me anything...")

if user_input:

    # user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # ----------------------------
    # CALL FASTAPI (with spinner)
    # ----------------------------
    try:
        with st.spinner("Thinking... 🤔"):

            response = requests.post(
                API_URL,
                json={"message": user_input},
                timeout=30
            )

        if response.status_code == 200:
            bot_reply = response.json()["reply"]
        else:
            try:
                detail = response.json().get("detail", response.text)
            except ValueError:
                detail = response.text
            bot_reply = f"❌ Error ({response.status_code}): {detail}"

    except requests.exceptions.Timeout:
        bot_reply = "❌ Request timed out. The backend took too long to respond."
    except requests.exceptions.ConnectionError:
        bot_reply = f"❌ Could not connect to backend at {BACKEND_URL}. Is it running?"
    except Exception as e:
        bot_reply = f"❌ Connection error: {str(e)}"

    # ----------------------------
    # BOT MESSAGE
    # ----------------------------
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_reply
    })