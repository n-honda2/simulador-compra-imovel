from fastapi import FastAPI

from app.routers import simulacao_router

# Instancia principal da aplicação FastAPI e a descreve para documentação automática.
app = FastAPI(
    title="API de Simulação de Financiamento de Imóvel",
    description="Uma API REST para simular cálculos de financiamento imobiliário no modelo da aMORA. Acesse /docs para a documentação interativa.",
    version="0.1.0",
)

# Inclui o roteador de simulação na aplicação principal.
app.include_router(simulacao_router.router)


# Endpoint raiz da API para boas-vindas e instruções de uso iniciais.
@app.get("/")
async def root():
    """
    Endpoint raiz da API.
    Retorna uma mensagem de boas-vindas e instrução para acessar a documentação.
    """
    return {"message": "Bem-vindo à API de Simulação de Financiamento! Acesse /docs para a documentação interativa."}
