# tests/unit/test_schemas.py
import pytest
from pydantic import ValidationError
from app.schemas.simulacao_base import SimulacaoRequest, SimulacaoResponse

def test_simulacao_request_valid_data():
    """
    Verifica se o modelo SimulacaoRequest valida corretamente
    dados de entrada que estão dentro dos limites esperados e tipos corretos.
    Espera-se que o objeto seja criado sem ValidationError.
    """
    data = {
        "valor_imovel": 500000.0,
        "percentual_entrada": 15.0,
        "anos_contrato": 3
    }
    request = SimulacaoRequest(**data)
    assert request.valor_imovel == 500000.0
    assert request.percentual_entrada == 15.0
    assert request.anos_contrato == 3

def test_simulacao_request_invalid_percentual_entrada_low():
    """
    Testa a validação de SimulacaoRequest com percentual_entrada
    abaixo do limite mínimo (5%). Espera-se que uma ValidationError seja levantada.
    """
    invalid_data = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 4.0, # Inválido
        "anos_contrato": 2
    }
    with pytest.raises(ValidationError): # Espera que uma ValidationError seja lançada
        SimulacaoRequest(**invalid_data)

def test_simulacao_request_invalid_percentual_entrada_high():
    """
    Testa a validação de SimulacaoRequest com percentual_entrada
    acima do limite máximo (20%). Espera-se que uma ValidationError seja levantada.
    """
    invalid_data = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 21.0, # Inválido
        "anos_contrato": 2
    }
    with pytest.raises(ValidationError):
        SimulacaoRequest(**invalid_data)

def test_simulacao_request_invalid_anos_contrato_low():
    """
    Testa a validação de SimulacaoRequest com anos_contrato
    abaixo do limite mínimo (1). Espera-se que uma ValidationError seja levantada.
    """
    invalid_data = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 10.0,
        "anos_contrato": 0 # Inválido
    }
    with pytest.raises(ValidationError):
        SimulacaoRequest(**invalid_data)

def test_simulacao_request_invalid_anos_contrato_high():
    """
    Testa a validação de SimulacaoRequest com anos_contrato
    acima do limite máximo (5). Espera-se que uma ValidationError seja levantada.
    """
    invalid_data = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 10.0,
        "anos_contrato": 6 # Inválido
    }
    with pytest.raises(ValidationError):
        SimulacaoRequest(**invalid_data)

def test_simulacao_request_invalid_valor_imovel():
    """
    Testa a validação de SimulacaoRequest com valor_imovel
    inválido (e.g., zero ou negativo). Espera-se que uma ValidationError seja levantada.
    """
    invalid_data = {
        "valor_imovel": 0.0, # Inválido
        "percentual_entrada": 10.0,
        "anos_contrato": 2
    }
    with pytest.raises(ValidationError):
        SimulacaoRequest(**invalid_data)

def test_simulacao_response_creation():
    """
    Verifica se o modelo SimulacaoResponse pode ser criado corretamente
    com os dados de saída esperados.
    """
    response = SimulacaoResponse(
        valor_entrada=50000.0,
        valor_financiado=450000.0,
        total_a_guardar=75000.0, 
        parcela_mensal=2083.33 
    )
    assert response.valor_entrada == 50000.0
    assert response.valor_financiado == 450000.0
    assert response.total_a_guardar == 75000.0
    assert response.parcela_mensal == 2083.33