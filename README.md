# simulador-compra-imovel
API REST que simula a compra de um imóvel no modelo de vendas da aMORA


## Passos para rodar localmente
Documentação muito ruim só pra não esquecer dps kkkkkkkkk
1. criar o venv:
2. dar source no ambiente virtual ``source venv/bin/activate.fish`` (eu uso fish, kd um se vira com seu shell ~~kd meu docker?~~)
3. instalar as dependências (listadas lá no venv_requirements.txt)
4. rodar o uvicorn (servidor web): ``uvicorn app.main:app --reload``