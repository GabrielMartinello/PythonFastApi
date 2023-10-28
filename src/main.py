import json
from fastapi import FastAPI, Request, Response
from datetime import datetime

app = FastAPI()
# teste= {
#   "id": 1,
#   "vaga": "vagaDesenvolvimento", 
#   "requisitos": "Linguagem Python, c++ e conhecimento em HTML",
#   "disponivel": "S"
# }

oportunidades = []
# oportunidades.append(teste)

@app.post("/cadastrar")
async def cadastrar(request: Request):
    body = await request.body()
    body = dict(json.loads(body))
    idVaga = 1
        
    if not len(oportunidades) == 0:     
        for vaga in oportunidades:
            idVaga += 1
            
    body["id"] = idVaga        
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

@app.delete("/vagapreenchida/{id}")
def deletarVaga(id:int):
    for vagas in oportunidades:
        if vagas.get("id") == id: 
            vagaPreenchida = vagas
            oportunidades.remove(vagaPreenchida)
      
    return {"vagapreenchida": "deu"}

