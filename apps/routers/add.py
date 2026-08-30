"""POST /calculate/add エンドポイント。"""

from fastapi import APIRouter

from apps.schemas import AddRequest, CalculationResponse

router = APIRouter()


@router.post("/calculate/add", response_model=CalculationResponse)
def add(request: AddRequest) -> CalculationResponse:
    """2つの正の整数を加算する。

    Parameters
    ----------
    request : AddRequest
        被加数 `a` と加数 `b`(いずれも正の整数)を含むリクエストボディ。

    Returns
    -------
    CalculationResponse
        `a + b` の計算結果を含むレスポンスボディ。
    """
    return CalculationResponse(
        operation="add",
        a=request.a,
        b=request.b,
        result=request.a + request.b,
    )
