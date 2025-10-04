import os
import sys
import csv

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.task1_maxflow.solver import run_solver  # noqa: E402

def test_maxflow_and_csv():
    maxf, path = run_solver()
    assert maxf == 115, f"Очікували max flow = 115, отримали {maxf}"
    assert os.path.exists(path), "CSV не створено"

    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = list(r)
        assert set(r.fieldnames) == {"Terminal", "Shop", "Flow"}  # type: ignore[arg-type]

    total = 0
    terms = set()
    shops = set()
    for row in rows:
        flow = int(row["Flow"])
        assert flow > 0
        total += flow
        terms.add(row["Terminal"])
        shops.add(row["Shop"])

    assert total == 115, f"Сума по CSV має дорівнювати 115, а не {total}"
    assert terms.issubset({"T1", "T2"})
    assert len(shops) == 14  # кожен магазин має позитивний потік
