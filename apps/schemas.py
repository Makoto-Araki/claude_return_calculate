from pydantic import BaseModel, PositiveInt


class AddRequest(BaseModel):
    a: PositiveInt
    b: PositiveInt


class CalculationResponse(BaseModel):
    operation: str
    a: int
    b: int
    result: int
