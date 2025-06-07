# tests/integration/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app # Importa sua aplicação FastAPI principal
from app.schemas.simulacao_base import SimulacaoResponse

# Cria uma instância do TestClient para sua aplicação.
client = TestClient(app)

def test_post_simulacao_success():
    """
    Verifica o endpoint POST /simulacao com um payload de requisição válido.
    Espera-se uma resposta HTTP 200 OK e que os dados de simulação retornados
    estejam corretos e no formato esperado pelo SimulacaoResponse.
    """
    payload = {
        "valor_imovel": 500000.0,
        "percentual_entrada": 10.0,
        "anos_contrato": 3
    }
    response = client.post("/simulacao", json=payload)

    # Verifica se o código de status HTTP é 200 (OK)
    assert response.status_code == 200
    data = response.json()

    # Valida a estrutura da resposta com o modelo Pydantic.
    SimulacaoResponse(**data)

    # Verifica se os valores calculados correspondem aos esperados (baseados na sua lógica de serviço)
    assert data["valor_entrada"] == 50000.0
    assert data["valor_financiado"] == 450000.0
    assert data["total_a_guardar"] == 75000.0 
    assert data["parcela_mensal"] == pytest.approx(2083.33, abs=0.01)

def test_post_simulacao_invalid_percentual_entrada():
    """
    Testa o endpoint POST /simulacao com percentual_entrada inválido (e.g., 4%).
    Espera-se uma resposta HTTP 422 Unprocessable Entity, pois a validação do Pydantic deve falhar.
    """
    payload = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 4.0, # Inválido (menor que 5)
        "anos_contrato": 2
    }
    response = client.post("/simulacao", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()
    assert "percentual_entrada" in str(response.json()) # Verifica se a mensagem de erro menciona o campo

def test_post_simulacao_invalid_anos_contrato():
    """
    Testa o endpoint POST /simulacao com anos_contrato inválido (e.g., 0).
    Espera-se uma resposta HTTP 422 Unprocessable Entity.
    """
    payload = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 10.0,
        "anos_contrato": 0 # Inválido (menor que 1)
    }
    response = client.post("/simulacao", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()
    assert "anos_contrato" in str(response.json())

def test_post_simulacao_missing_field():
    """
    Testa o endpoint POST /simulacao com um campo obrigatório faltando (e.g., 'anos_contrato').
    Espera-se uma resposta HTTP 422 Unprocessable Entity.
    """
    payload = {
        "valor_imovel": 100000.0,
        "percentual_entrada": 10.0
        # anos_contrato está faltando
    }
    response = client.post("/simulacao", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()
    assert "Field required" in str(response.json())

def test_post_simulacao_invalid_json_format():
    """
    Testa o endpoint POST /simulacao com um JSON mal formatado ou com tipo de dado incorreto.
    Espera-se uma resposta HTTP 422 Unprocessable Entity.
    """
    # Exemplo de payload com tipo de dado errado para valor_imovel (string em vez de número)
    payload = {
        "valor_imovel": "abc", # Inválido
        "percentual_entrada": 10.0,
        "anos_contrato": 2
    }
    response = client.post("/simulacao", json=payload)

    assert response.status_code == 422
    assert "detail" in response.json()
    assert "Input should be a valid number, unable to parse string as a number" in str(response.json()) # Pydantic reporta erro de tipo