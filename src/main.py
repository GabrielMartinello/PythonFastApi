import json
from fastapi import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()
teste= {
  "vaga": "vagaDesenvolvimento", 
  "requisitos": "Linguagem Python, c++ e conhecimento em HTML",
  "disponivel": "S"
}

oportunidades = []
oportunidades.append(teste)

@app.post("/cadastrar")
async def cadastrar(request: Request):
    body = await request.body()
    body = dict(json.loads(body))
    body["data_hora_criacao"] = datetime.now()
    oportunidades.append(body)
    return body

@app.get("/vagasDisponiveis")
def lista_vagas_disponiveis():
    vagasDisponiveis = []
    for vagas in oportunidades:
        if vagas.get("disponivel") == 'S':
            vagasDisponiveis.append(vagas)

    return {"Vagas": vagasDisponiveis}



