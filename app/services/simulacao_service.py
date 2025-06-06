import math
from app.schemas.simulacao_base import SimulacaoRequest, SimulacaoResponse

def calcular_simulacao(request_data: SimulacaoRequest) -> SimulacaoResponse:
    """
    Documentação da fução de simulação
    """

    valor_entrada = 0.0
    valor_financiado = 0.0
    total_a_guardar = 0.0
    parcela_mensal = 0.0

    # Implementar dps lógica do cálculo da simulação com os dados do objeot SImulacaoRequest

    response = SimulacaoResponse(
        valor_entrada=valor_entrada,
        valor_financiado=valor_financiado,
        total_a_guardar=total_a_guardar,
        parcela_mensal=parcela_mensal
    )

    return response
