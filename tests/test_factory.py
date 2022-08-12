import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from factory import create_app, register_routers


@pytest.fixture
def app():
    _app = create_app()
    register_routers(_app, "views")
    yield _app


@pytest.fixture
def client(app: FastAPI): # pylint:disable=redefined-outer-name
    yield TestClient(app)


def test_status(client: TestClient): # pylint:disable=redefined-outer-name
    resp = client.get("/common/status")
    assert resp.json() == {"code": 0, "data": {"status": "服务正常"}, "msg": "", "success": True}
