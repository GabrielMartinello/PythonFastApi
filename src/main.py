import json
from fastapi import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()

valores = []

@app.get("/")
def hello_world():
    return {"Teste": valores}

@app.post("/cadastrar")
async def responda_outro(request: Request):
    body = await request.body()
    body = dict(json.loads(body))
    body["data_hora_criacao"] = datetime.now()
    valores.append(body)
    return body

