import json
from fastapi import FastAPI, Request, Response
from datetime import datetime
import uuid

app = FastAPI()

teste = [
    {
        "id": uuid.uuid4(),
        "vaga": "Desenvolvedor Java Pl", 
        "requisitos": "Computação em Nuvem (AWS, Azure e Google Cloud), Microservices, Conteiners, Docker e Kubernets, Frameworks de Data Bus / Mensageria, como Apache Kafka e RabbitMQ, etc......",
        "disponivel": True
    },
    {
         "id": uuid.uuid4(),
         "vaga": "Desenvolvedor Python", 
         "requisitos": "Experiência com estruturas Python (por exemplo, Django, Flask, Bottle) e sei lá oq, SQL, JS",
         "disponivel": True
    } 
]

oportunidades = []
oportunidades.extend(teste)

@app.post("/cadastrar")
async def cadastrar(request: Request):
    body = await request.body()
    body = dict(json.loads(body))

    #usado para gerar um identificador único        
    body["id"] = uuid.uuid4()        
    body["data_hora_criacao"] = datetime.now()
    oportunidades.append(body)
    return body

@app.get("/vagasDisponiveis")
def lista_vagas_disponiveis():
    vagasDisponiveis = []
    
    for vagas in oportunidades:
        if vagas.get("disponivel") == True:
            vagasDisponiveis.append(vagas)

    if not vagasDisponiveis:
        return {"erro": "Não existem vagas disponíveis"}                     

    return {"Vagas": vagasDisponiveis}

@app.patch("/preencherVaga/{id}")
async def preencherVaga(id: str, request: Request):
    vagaPreencher = None

    if not is_valid_uuid(id):
        return {"erro": "Id inválido!"}
    
    if not oportunidades:
        return {"erro": "Não existem vagas para preencher!"}
    
    body = await request.body()
    body = json.loads(body)

    for vaga in oportunidades:
        id = uuid.UUID(str(id))
        if vaga.get("id") == id: 
            vagaPreencher = vaga
            break

    if vagaPreencher != None:
        indice = oportunidades.index(vagaPreencher)
        oportunidades[indice]["disponivel"] = body.get("disponivel")
        return {"vagaPreenchida": oportunidades[indice]}


    return Response(content= {"erro": "Não foi possível encontrar a vaga"},
                        status_code=404,
                        media_type="application/json")

@app.delete("/deletarVaga/{id}")
def deletarVaga(id):
    vagaPreenchida = None

    #Verifico se o id é válido
    if not is_valid_uuid(id):
        return {"erro": "Id inválido!"}
    
    if not oportunidades:
        return {"erro": "Não existem vagas para excluir!"}

    for vaga in oportunidades:
        id = uuid.UUID(str(id))
        if vaga.get("id") == id: 
            vagaPreenchida = vaga
            break

    if vagaPreenchida != None:
         oportunidades.remove(vagaPreenchida)
         return {"vagaDeletada": vagaPreenchida}

    return Response(content= {"erro": "Não foi possível encontrar a vaga"},
                        status_code=404,
                        media_type="application/json")


def is_valid_uuid(id):
    try:
        uuid.UUID(str(id))
        return True
    except ValueError:
        return False