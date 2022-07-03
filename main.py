import os
import pickle

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# ------------------------------------------------------------------------------- #

# READ_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Files")

# questions = pickle.load(open(os.path.join(READ_PATH, "questions.pkl"), "rb"))
# answers   = pickle.load(open(os.path.join(READ_PATH, "answers.pkl"), "rb"))

# history: list = []

# ------------------------------------------------------------------------------- #

VERSION = "0.0.1-alpha"

STATIC_PATH = "static"

questions = pickle.load(open(os.path.join(STATIC_PATH, "questions.pkl"), "rb"))
answers   = pickle.load(open(os.path.join(STATIC_PATH, "answers.pkl"), "rb"))

origins = [
    "http://localhost:10001",
]

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return "Root Path for Bot API", 


@app.get("/wakeup")
async def root():
    return "Awake", 


@app.get("/chatbot-version")
async def chatbot_version():
    return {
        "version" : VERSION,
    }


@app.get("/telephone-banking")
async def telephone_banking():
    return {
        "statusCode" : 200,
        "statusText" : "Telephone Banking FAQ Fetch Successful",
        "questions" : questions["telephone_banking"],
        "answers" : answers["telephone_banking"]
    }


@app.get("/mobile-banking")
async def mobile_banking():
    return {
        "statusCode" : 200,
        "statusText" : "Mobile Banking FAQ Fetch Successful",
        "questions" : questions["mobile_banking"],
        "answers" : answers["mobile_banking"]
    }


@app.get("/internet-banking")
async def internet_banking():
    return {
        "statusCode" : 200,
        "statusText" : "Internet Banking FAQ Fetch Successful",
        "questions" : questions["internet_banking"],
        "answers" : answers["internet_banking"]
    }
