# tests/unit/test_services.py
import pytest

from app.schemas.simulacao_base import SimulacaoRequest
from app.services.simulacao_service import calcular_simulacao


def test_calcular_simulacao_cenario_padrao():
    """
    Valida a função calcular_simulacao para um cenário de financiamento
    típico (valor do imóvel: 500.000, entrada: 10%, anos: 3).
    Verifica se os valores calculados (entrada, financiado, guardar, parcela)
    correspondem aos esperados com base na lógica de cálculo.
    """
    request_data = SimulacaoRequest(valor_imovel=500000.0, percentual_entrada=10.0, anos_contrato=3)

    expected_valor_entrada = 50000  # 10% de 500000
    expected_valor_financiado = 450000  # valor_imovel - valor_entrada
    expected_total_a_guardar = 75000  # 15% de valor_imovel
    expected_parcela_mensal = 2083.33  # total_a_guardar / (anos_contrato * 12)

    actual_response = calcular_simulacao(request_data)

    # Usamos pytest.approx para floats devido a possíveis imprecisões de ponto flutuante
    assert actual_response.valor_entrada == pytest.approx(expected_valor_entrada, abs=0.01)
    assert actual_response.valor_financiado == pytest.approx(expected_valor_financiado, abs=0.01)
    assert actual_response.total_a_guardar == pytest.approx(expected_total_a_guardar, abs=0.01)
    assert actual_response.parcela_mensal == pytest.approx(expected_parcela_mensal, abs=0.01)
