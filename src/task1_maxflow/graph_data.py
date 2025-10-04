from __future__ import annotations
from typing import Dict, List, Tuple

# Бізнес-вершини:
# 2 термінали:   T1, T2
# 4 склади:      W1..W4
# 14 магазинів:  S1..S14
# Технічні вершини: SRC, SNK

Terminals: List[str] = ["T1", "T2"]
Warehouses: List[str] = [f"W{i}" for i in range(1, 5)]
Shops: List[str] = [f"S{i}" for i in range(1, 15)]

SRC = "SRC"
SNK = "SNK"

# Попит магазинів (сума = 115)
shop_caps: Dict[str, int] = {
    "S1": 10, "S2": 8,  "S3": 7,  "S4": 9,
    "S5": 6,  "S6": 7,  "S7": 8,  "S8": 9,
    "S9": 6,  "S10": 8, "S11": 9, "S12": 6,
    "S13": 8, "S14": 14,
}

# Термінали → склади (вхідні ємності складів)
# ВАЖЛИВО: сума вхідних у W2 >= сумі його виходів (S5..S8,S11=39),
# тож ставимо 39 (а не 35), щоб сумарний потік досягав 115.
terminal_to_warehouse_caps: List[Tuple[str, str, int]] = [
    ("T1", "W1", 40),
    ("T1", "W2", 39),  # покриває 39 попиту з W2
    ("T2", "W3", 25),
    ("T2", "W4", 30),
]

# Склади → магазини
warehouse_to_shop_caps: List[Tuple[str, str, int]] = [
    # W1: S1..S4 (разом 34)
    ("W1", "S1", shop_caps["S1"]),
    ("W1", "S2", shop_caps["S2"]),
    ("W1", "S3", shop_caps["S3"]),
    ("W1", "S4", shop_caps["S4"]),

    # W2: S5..S8 (30) + S11 (9) = 39
    ("W2", "S5", shop_caps["S5"]),
    ("W2", "S6", shop_caps["S6"]),
    ("W2", "S7", shop_caps["S7"]),
    ("W2", "S8", shop_caps["S8"]),
    ("W2", "S11", shop_caps["S11"]),

    # W3: S9 (6), S10 (8) = 14 (вхід W3=25 з запасом)
    ("W3", "S9", shop_caps["S9"]),
    ("W3", "S10", shop_caps["S10"]),

    # W4: S12 (6), S13 (8), S14 (14) = 28 (вхід W4=30 з запасом)
    ("W4", "S12", shop_caps["S12"]),
    ("W4", "S13", shop_caps["S13"]),
    ("W4", "S14", shop_caps["S14"]),
]

def build_edges() -> List[Tuple[str, str, int]]:
    edges: List[Tuple[str, str, int]] = []

    # Джерело → термінали (достатньо великі, щоб вузьким місцем були магазини сумарно на 115)
    # T1 потребує щонайменше 40+39=79, ставимо 80; T2 потребує 25+30=55, ставимо 60.
    edges += [(SRC, "T1", 80), (SRC, "T2", 60)]

    # Термінали → склади
    edges += terminal_to_warehouse_caps

    # Склади → магазини
    edges += warehouse_to_shop_caps

    # Магазини → стік (обмеження попиту)
    edges += [(s, SNK, cap) for s, cap in shop_caps.items()]

    return edges
