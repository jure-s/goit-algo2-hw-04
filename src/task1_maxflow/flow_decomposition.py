from __future__ import annotations
from typing import Dict, List, Tuple
from .graph_data import Warehouses, Shops

# За побудовою: T1 постачає W1,W2; T2 — W3,W4.
# Для кожного магазину дивимось з якого складу прийшов позитивний потік і мапимо склад -> термінал.

def decompose_terminal_to_shop(flow: Dict[str, Dict[str, int]]) -> List[Tuple[str, str, int]]:
    w2t = {}
    for w in Warehouses:
        if flow.get("T1", {}).get(w, 0) > 0:
            w2t[w] = "T1"
        elif flow.get("T2", {}).get(w, 0) > 0:
            w2t[w] = "T2"
        else:
            # резервне правило за назвою складу (на випадок нульового потоку з термінала)
            w2t[w] = "T1" if w in ("W1", "W2") else "T2"

    rows: List[Tuple[str, str, int]] = []
    for w in Warehouses:
        for s in Shops:
            f = flow.get(w, {}).get(s, 0)
            if f > 0:
                rows.append((w2t[w], s, f))
    return rows
