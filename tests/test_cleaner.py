from fastapi.testclient import TestClient
from app.main import app
import os
import pandas as pd

client = TestClient(app)

def test_cleaning(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))

    df = pd.DataFrame({"A":[1,1, None], "B":[None,2,2]})
    file = tmp_path / "abc.csv"
    df.to_csv(file, index=False)

    res = client.post("/clean", json={"dataset_id":"abc"})
    assert res.status_code == 200
    data = res.json()
    assert data["report"]["duplicates_removed"] == 1
    assert any(int(v) > 0 for v in data["report"]["missing_values_filled"].values())