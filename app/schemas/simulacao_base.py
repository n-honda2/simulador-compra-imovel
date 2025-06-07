from pydantic import BaseModel, Field


# Classe
class SimulacaoRequest(BaseModel):
    valor_imovel: float = Field(..., gt=0, description="Valor total do imóvel.")
    percentual_entrada: float = Field(..., ge=5, le=20, description="Percentual da entrada (entre 5 e 20).")
    anos_contrato: int = Field(..., ge=1, le=5, description="Número de anos do contrato (entre 1 e 5).")


class SimulacaoResponse(BaseModel):
    valor_entrada: float = Field(..., description="Valor da entrada calculada.")
    valor_financiado: float = Field(..., description="Valor total a ser financiado.")
    total_a_guardar: float = Field(
        ..., description="Valor totoal guardado no fim do contrato (? rever o modelo de negócios depois)."
    )
    parcela_mensal: float = Field(
        ..., description="Valor estimado da parcela mensal do financiamento no modelo de negócios da aMORA."
    )
