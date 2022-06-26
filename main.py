import os
import pickle

from fastapi import FastAPI

# ------------------------------------------------------------------------------- #

VERSION = "0.0.1-alpha"
READ_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Files")

questions = pickle.load(open(os.path.join(READ_PATH, "questions.pkl"), "rb"))
answers   = pickle.load(open(os.path.join(READ_PATH, "answers.pkl"), "rb"))

history: list = []

# ------------------------------------------------------------------------------- #

app = FastAPI()


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
        "questions" : questions["telephone_banking"],
        "answers" : answers["telephone_banking"]
    }


@app.get("/mobile-banking")
async def mobile_banking():
    return {
        "questions" : questions["mobile_banking"],
        "answers" : answers["mobile_banking"]
    }


@app.get("/internet-banking")
async def internet_banking():
    return {
        "questions" : questions["internet_banking"],
        "answers" : answers["internet_banking"]
    }
