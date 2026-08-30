from fastapi import APIRouter

from apps.schemas import AddRequest, CalculationResponse

router = APIRouter()


@router.post("/calculate/add", response_model=CalculationResponse)
def add(request: AddRequest) -> CalculationResponse:
    return CalculationResponse(
        operation="add",
        a=request.a,
        b=request.b,
        result=request.a + request.b,
    )
