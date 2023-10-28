import json
from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}


