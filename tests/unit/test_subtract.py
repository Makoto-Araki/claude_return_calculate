"""POST /calculate/subtract のユニットテスト。"""

import pytest
from fastapi.testclient import TestClient

from apps.main import app

client = TestClient(app)


def test_subtract_success():
    """正の整数同士の減算が200 OKで正しい結果を返すことを検証する。"""
    response = client.post("/calculate/subtract", json={"a": 10, "b": 3})

    assert response.status_code == 200
    assert response.json() == {
        "operation": "subtract",
        "a": 10,
        "b": 3,
        "result": 7,
    }


def test_subtract_negative_result():
    """a < b の場合に結果が負数として正しく返ることを検証する。"""
    response = client.post("/calculate/subtract", json={"a": 3, "b": 10})

    assert response.status_code == 200
    assert response.json() == {
        "operation": "subtract",
        "a": 3,
        "b": 10,
        "result": -7,
    }


@pytest.mark.parametrize("payload", [{"a": 0, "b": 3}, {"a": 10, "b": 0}])
def test_subtract_rejects_zero(payload):
    """a/b が0の場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に `0` を含むリクエストボディ。
    """
    response = client.post("/calculate/subtract", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": -1, "b": 3}, {"a": 10, "b": -5}])
def test_subtract_rejects_negative(payload):
    """a/b が負数の場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に負数を含むリクエストボディ。
    """
    response = client.post("/calculate/subtract", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": 1.5, "b": 3}, {"a": 10, "b": 2.5}])
def test_subtract_rejects_float(payload):
    """a/b が小数の場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に小数を含むリクエストボディ。
    """
    response = client.post("/calculate/subtract", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": "foo", "b": 3}, {"a": 10, "b": "bar"}])
def test_subtract_rejects_non_numeric(payload):
    """a/b が数値でない場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` に非数値を含むリクエストボディ。
    """
    response = client.post("/calculate/subtract", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"b": 3}, {"a": 10}, {}])
def test_subtract_rejects_missing_field(payload):
    """a/b が欠落している場合に422が返ることを検証する。

    Parameters
    ----------
    payload : dict
        `a` または `b` が欠落したリクエストボディ。
    """
    response = client.post("/calculate/subtract", json=payload)

    assert response.status_code == 422
