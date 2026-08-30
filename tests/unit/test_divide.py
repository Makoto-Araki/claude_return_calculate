"""POST /calculate/divide のユニットテスト。"""

import pytest
from fastapi.testclient import TestClient

from apps.main import app

client = TestClient(app)


def test_divide_success():
    """割り切れる正の整数同士の除算が200 OKで正しい結果を返すことを検証する。"""
    response = client.post("/calculate/divide", json={"a": 10, "b": 5})

    assert response.status_code == 200
    assert response.json() == {
        "operation": "divide",
        "a": 10,
        "b": 5,
        "result": 2.0,
    }


def test_divide_success_non_terminating():
    """割り切れない除算の結果が小数(float)で返ることを検証する。"""
    response = client.post("/calculate/divide", json={"a": 10, "b": 3})

    assert response.status_code == 200
    body = response.json()
    assert body["operation"] == "divide"
    assert body["a"] == 10
    assert body["b"] == 3
    assert body["result"] == pytest.approx(10 / 3)


@pytest.mark.parametrize("payload", [{"a": 0, "b": 3}, {"a": 10, "b": 0}])
def test_divide_rejects_zero(payload):
    """a/b が0の場合に422が返ることを検証する(独自の400エラーは実装しない)。

    Parameters
    ----------
    payload : dict
        `a` または `b` に `0` を含むリクエストボディ。
    """
    response = client.post("/calculate/divide", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": -1, "b": 3}, {"a": 10, "b": -5}])
def test_divide_rejects_negative(payload):
    """a/b が負数の場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に負数を含むリクエストボディ。
    """
    response = client.post("/calculate/divide", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": 1.5, "b": 3}, {"a": 10, "b": 2.5}])
def test_divide_rejects_float(payload):
    """a/b が小数の場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に小数を含むリクエストボディ。
    """
    response = client.post("/calculate/divide", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": "foo", "b": 3}, {"a": 10, "b": "bar"}])
def test_divide_rejects_non_numeric(payload):
    """a/b が数値でない場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に非数値を含むリクエストボディ。
    """
    response = client.post("/calculate/divide", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"b": 3}, {"a": 10}, {}])
def test_divide_rejects_missing_field(payload):
    """a/b が欠落している場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` が欠落したリクエストボディ。
    """
    response = client.post("/calculate/divide", json=payload)

    assert response.status_code == 422
