from __future__ import annotations
from typing import Tuple
from .graph_data import SRC, SNK, build_edges
from .edmonds_karp import EdmondsKarp
from .flow_decomposition import decompose_terminal_to_shop
from ..common.io_utils import save_terminal_shop_csv

CSV_PATH = "data/terminal_shop_flow.csv"

def run_solver() -> Tuple[int, str]:
    edges = build_edges()
    ek = EdmondsKarp(edges)
    maxf = ek.max_flow(SRC, SNK)

    # Декомпозиція Terminal → Shop
    rows = decompose_terminal_to_shop(ek.flow)
    rows = [r for r in rows if r[2] > 0]
    save_terminal_shop_csv(rows, CSV_PATH)

    return maxf, CSV_PATH

if __name__ == "__main__":
    mf, path = run_solver()
    print(f"Max flow = {mf}. CSV saved to {path}")
