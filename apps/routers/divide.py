"""POST /calculate/divide エンドポイント。"""

from fastapi import APIRouter

from apps.schemas import DivideRequest, DivideResponse

router = APIRouter()


@router.post("/calculate/divide", response_model=DivideResponse)
def divide(request: DivideRequest) -> DivideResponse:
    """2つの正の整数を除算する。

    Parameters
    ----------
    request : DivideRequest
        被除数 `a` と除数 `b`(いずれも正の整数)を含むリクエストボディ。

    Returns
    -------
    DivideResponse
        `a / b` の計算結果を含むレスポンスボディ。
    """
    return DivideResponse(
        operation="divide",
        a=request.a,
        b=request.b,
        result=request.a / request.b,
    )
