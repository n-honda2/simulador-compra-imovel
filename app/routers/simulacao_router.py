from fastapi import APIRouter, HTTPException, status
from app.schemas.simulacao_base import SimulacaoRequest, SimulacaoResponse
from app.services.simulacao_service import calcular_simulacao

# Instância de APIRouter com o prefixo indicado e a tag para documentação automática
router = APIRouter(prefix="/simulacao", tags=["Simulacao"])

# Definição do endpoint que recebe request do tipo POST e modelo de resposta a partir da schema base de resposta
@router.post("/", response_model=SimulacaoResponse)
async def simular_financiamento(request: SimulacaoRequest):
    """
    Simula um financiamento imobiliário com base nos parâmetros fornecidos.

    **Parâmetros de Requisição (JSON Body):**
    - `valor_imovel` (float): O valor total do imóvel. Deve ser um número positivo.
    - `percentual_entrada` (float): O percentual do valor do imóvel que será dado como entrada.
      Deve estar entre 5 e 20 (inclusive).
    - `anos_contrato` (int): O número de anos do contrato de financiamento.
      Deve estar entre 1 e 5 (inclusive).

    **Respostas:**
    - **200 OK:** Retorna um objeto `SimulacaoResponse` contendo os detalhes calculados do financiamento.
      Exemplo de resposta:
      ```json
      {
        "valor_entrada": 20000.00,
        "valor_financiado": 380000.00,
        "total_a_guardar": 60000.00,
        "parcela_mensal": 1666.67
      }
      ```
    - **422 Unprocessable Entity:** Ocorre se os parâmetros de entrada não passarem na validação
      (ex: `percentual_entrada` fora do intervalo, campo obrigatório faltando, tipo de dado incorreto).
      O corpo da resposta JSON conterá detalhes sobre o erro de validação.
    - **500 Internal Server Error:** Ocorre se um erro inesperado acontecer durante o processamento da simulação
      no servidor. Isso pode indicar um problema na lógica de cálculo ou na infraestrutura.

    **Notas de Cálculo:**
    - `valor_entrada` = `valor_imovel` * (`percentual_entrada` / 100)
    - `valor_financiado` = `valor_imovel` - `valor_entrada`
    - `total_a_guardar` = `valor_imovel` * 0.15 (15% do valor do imóvel)
    - `parcela_mensal` = `total_a_guardar` / (`anos_contrato` * 12)

    ---
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