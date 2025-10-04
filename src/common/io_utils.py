from __future__ import annotations
import csv
from pathlib import Path
from typing import Iterable, Tuple

def save_terminal_shop_csv(rows: Iterable[Tuple[str, str, int]], path: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Terminal", "Shop", "Flow"])
        for term, shop, val in rows:
            w.writerow([term, shop, val])
