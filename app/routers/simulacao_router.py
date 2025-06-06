from fastapi import APIRouter, HTTPException, status
from app.schemas.simulacao_base import SimulacaoRequest, SimulacaoResponse
from app.services.simulacao_service import calcular_simulacao

# Instância de APIRouter com o prefixo indicado e a tag para documentação automática
router = APIRouter(prefix="/simulacao", tags=["Simulacao"])

# Definição do endpoint que recebe request do tipo POST e modelo de resposta a partir da schema base de resposta
@router.post("/", response_model=SimulacaoResponse)
async def simular_financiamento(request: SimulacaoRequest):
    """
    Documentação do endpoint
    """
    try:
        # Utiliza a função de serviço para processar a simulação e retornar o resultado
        result = calcular_simulacao(request)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro interno ao processar a simulação: {e}"
        )