"""POST /calculate/subtract エンドポイント。"""

from fastapi import APIRouter

from apps.schemas import CalculationResponse, SubtractRequest

router = APIRouter()


@router.post("/calculate/subtract", response_model=CalculationResponse)
def subtract(request: SubtractRequest) -> CalculationResponse:
    """2つの正の整数を減算する。

    Parameters
    ----------
    request : SubtractRequest
        被減数 `a` と減数 `b`(いずれも正の整数)を含むリクエストボディ。

    Returns
    -------
    CalculationResponse
        `a - b` の計算結果を含むレスポンスボディ。
    """
    return CalculationResponse(
        operation="subtract",
        a=request.a,
        b=request.b,
        result=request.a - request.b,
    )
