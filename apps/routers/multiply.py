"""POST /calculate/multiply エンドポイント。"""

from fastapi import APIRouter

from apps.schemas import CalculationResponse, MultiplyRequest

router = APIRouter()


@router.post("/calculate/multiply", response_model=CalculationResponse)
def multiply(request: MultiplyRequest) -> CalculationResponse:
    """2つの正の整数を乗算する。

    Parameters
    ----------
    request : MultiplyRequest
        被乗数 `a` と乗数 `b`(いずれも正の整数)を含むリクエストボディ。

    Returns
    -------
    CalculationResponse
        `a * b` の計算結果を含むレスポンスボディ。
    """
    return CalculationResponse(
        operation="multiply",
        a=request.a,
        b=request.b,
        result=request.a * request.b,
    )
