import os
import sys
from fastapi.testclient import TestClient

# Ensure repo root is on sys.path so we can import `src` package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.app import app


client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # spot check an expected activity
    assert "Chess Club" in data


def test_root_redirect_and_static():
    resp = client.get("/")
    # root redirects to /static/index.html, TestClient may return 307/308
    assert resp.status_code in (200, 307, 308)
    resp2 = client.get("/static/index.html")
    assert resp2.status_code == 200
