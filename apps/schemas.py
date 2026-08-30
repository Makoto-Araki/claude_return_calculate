"""四則演算エンドポイントのリクエスト/レスポンスPydanticモデル。"""

from pydantic import BaseModel, PositiveInt


class AddRequest(BaseModel):
    """加算リクエストボディ。

    Attributes
    ----------
    a : PositiveInt
        被加数。正の整数(> 0)のみ許容する。
    b : PositiveInt
        加数。正の整数(> 0)のみ許容する。
    """

    a: PositiveInt
    b: PositiveInt


class CalculationResponse(BaseModel):
    """四則演算エンドポイント共通のレスポンスボディ。

    Attributes
    ----------
    operation : str
        実行した演算名(例: "add")。
    a : int
        1つ目のオペランド。
    b : int
        2つ目のオペランド。
    result : int
        演算結果。
    """

    operation: str
    a: int
    b: int
    result: int
