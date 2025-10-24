"""
Smoke tests for Mergington High School API

This script checks basic API endpoints for expected responses.
"""
import requests

BASE_URL = "http://localhost:8000"

def test_root_redirect():
    resp = requests.get(f"{BASE_URL}/", allow_redirects=False)
    assert resp.status_code in (307, 308), f"Expected redirect, got {resp.status_code}"

def test_activities():
    resp = requests.get(f"{BASE_URL}/activities")
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    data = resp.json()
    assert isinstance(data, dict), "Activities should be a dict"
    assert "Chess Club" in data, "Chess Club missing"

if __name__ == "__main__":
    test_root_redirect()
    test_activities()
    print("Smoke tests passed.")