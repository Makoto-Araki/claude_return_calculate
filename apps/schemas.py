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


class SubtractRequest(BaseModel):
    """減算リクエストボディ。

    Attributes
    ----------
    a : PositiveInt
        被減数。正の整数(> 0)のみ許容する。
    b : PositiveInt
        減数。正の整数(> 0)のみ許容する。
    """

    a: PositiveInt
    b: PositiveInt


class MultiplyRequest(BaseModel):
    """乗算リクエストボディ。

    Attributes
    ----------
    a : PositiveInt
        被乗数。正の整数(> 0)のみ許容する。
    b : PositiveInt
        乗数。正の整数(> 0)のみ許容する。
    """

    a: PositiveInt
    b: PositiveInt


class DivideRequest(BaseModel):
    """除算リクエストボディ。

    Attributes
    ----------
    a : PositiveInt
        被除数。正の整数(> 0)のみ許容する。
    b : PositiveInt
        除数。正の整数(> 0)のみ許容する。
    """

    a: PositiveInt
    b: PositiveInt


class DivideResponse(BaseModel):
    """除算エンドポイント専用のレスポンスボディ。

    割り切れない場合に商が小数となるため、`result` は `int` ではなく `float` を用いる。

    Attributes
    ----------
    operation : str
        実行した演算名(常に "divide")。
    a : int
        被除数。
    b : int
        除数。
    result : float
        演算結果(a / b)。
    """

    operation: str
    a: int
    b: int
    result: float


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
