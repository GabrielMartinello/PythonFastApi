# TrabalhoCezarPythao
Trabalho do cezar

Executar o seguintes comandos:

Abrir o terminal no git bash para pegar o terminal Linux;
- pip install "fastapi[all]"
- rodar o projeto: uvicorn src.main:app --reload

O objetivo deste projeto era simplificar o processo de um empresa que realiza os cadastros das vagas via planilha EXCEL. A empresa precisa de uma API REST para operações CRUD  (Create, Retrieve, Update e Delete) da vaga, contendo título da vaga, requisitos da vaga e data de criação. Deve listar somente as vagas que estão em aberto.

O projeto foi desenvolvido com python, utilizando a biblioteca fastapi para realizar API's Rest.

Para rodar o projeto é necessário rodar o comando pip install "fastapi[all]" no terminal do linux, se estiver rodando no windows, abrir o git bash e executar o comando.


Rota para indisponibilizar vagas
![Alt text](/assets/AlterarVagas.png?raw=true "AlterarVafgas.png")

Rota para realizar o cadastro das vagas que estão disponíveis ou que vão estar disponíveis futuramente
![Alt text](/assets/cadastrarVagas.png?raw=true "AlterarVafgas.png")

Rota para deletar as vagas
![Alt text](/assets/DeletarVagas.png?raw=true "AlterarVafgas.png")

Rota para alterar as vagas para disponível ou indisponível
![Alt text](/assets/ListarVagasDisponiveis.png?raw=true "AlterarVafgas.png")

Para realizar a indisponibilidade da vaga, foi desenvolvido uma rota para isso, que é passado na url o id da, e no body passa o valor true ou false para disponibilizar ou indisponibilizar a vaga.

Foi realizado todas as validações seguindo a opão número 4 - API de vagas de emprego

