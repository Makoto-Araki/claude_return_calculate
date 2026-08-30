import pytest
from fastapi.testclient import TestClient

from apps.main import app

client = TestClient(app)


def test_add_success():
    response = client.post("/calculate/add", json={"a": 10, "b": 3})

    assert response.status_code == 200
    assert response.json() == {
        "operation": "add",
        "a": 10,
        "b": 3,
        "result": 13,
    }


@pytest.mark.parametrize("payload", [{"a": 0, "b": 3}, {"a": 10, "b": 0}])
def test_add_rejects_zero(payload):
    response = client.post("/calculate/add", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": -1, "b": 3}, {"a": 10, "b": -5}])
def test_add_rejects_negative(payload):
    response = client.post("/calculate/add", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": 1.5, "b": 3}, {"a": 10, "b": 2.5}])
def test_add_rejects_float(payload):
    response = client.post("/calculate/add", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"a": "foo", "b": 3}, {"a": 10, "b": "bar"}])
def test_add_rejects_non_numeric(payload):
    response = client.post("/calculate/add", json=payload)

    assert response.status_code == 422


@pytest.mark.parametrize("payload", [{"b": 3}, {"a": 10}, {}])
def test_add_rejects_missing_field(payload):
    response = client.post("/calculate/add", json=payload)

    assert response.status_code == 422
