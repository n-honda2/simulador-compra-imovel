# Dockerfile
# Define a imagem base: Python 3.9 em uma distribuição Debian leve (slim-buster).
# É leve e contém o Python e o pip.
FROM python:3.10-slim-buster

# Define o diretório de trabalho dentro do contêiner.
# Todos os comandos subsequentes serão executados a partir deste diretório.
WORKDIR /app

# Copia o arquivo de dependências (requirements.txt) para o diretório de trabalho no contêiner.
# Copiamos apenas este arquivo primeiro para aproveitar o cache do Docker:
# se requirements.txt não mudar, este passo e o próximo não serão reexecutados.
COPY venv_requirements.txt .

# Instala as dependências Python listadas em requirements.txt.
# --no-cache-dir: Reduz o tamanho final da imagem ao não guardar o cache do pip.
# -r: Lê as dependências de um arquivo.
RUN pip install --no-cache-dir -r venv_requirements.txt

# Copia o restante do código da sua aplicação (a pasta 'app' e a pasta 'tests') para o contêiner.
# Isso deve ser feito depois de instalar as dependências para otimizar o cache da imagem.
COPY app/ app/
COPY tests/ tests/

# Expõe a porta em que a aplicação FastAPI irá rodar.
# Esta é a porta interna do contêiner.
EXPOSE 8000

# Define o comando padrão que será executado quando o contêiner for iniciado.
# - 'app.main:app': Indica ao Uvicorn para rodar a instância 'app' do FastAPI no módulo 'main' dentro do pacote 'app'.
# - '--host 0.0.0.0': Permite que a aplicação seja acessível de qualquer interface de rede (necessário para Docker).
# - '--port 8000': Define a porta interna do contêiner onde a aplicação vai escutar.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]