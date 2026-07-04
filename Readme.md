python -m venv venv

        it will create  venv folder in workspace (virtual envi ronment)

venv\Scripts\activate

    Activate 

pip install -r requirements.txt
pip list

mkdir app
mkdir tests
mkdir app\routes
mkdir app\services
mkdir app\tools
mkdir app\prompts
mkdir app\config
mkdir app\models
mkdir app\utils

Folder	Purpose
app/	Main application code
routes/	API endpoints (URLs)
services/	Business logic
tools/	AI tools/functions (like getting weather)
models/	Data models for requests/responses
config/	Configuration and settings
utils/	Shared helper functions
prompts/	System prompts for the AI
tests/	Unit and integration tests

uvicorn app.main:app --reload

uvicorn → Starts the ASGI server.
app.main → Refers to the main.py file inside the app folder.
:app → Uses the app = FastAPI() object from that file.
--reload → Automatically restarts the server whenever you save changes.

1c758b06485c43f45f04af8ad8d37294