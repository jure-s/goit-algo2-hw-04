from __future__ import annotations
import sys
import csv
from pathlib import Path


def run_task2() -> None:
    # Завдання 2 (Trie): демо з assert'ами + невелика вітрина результатів
    from src.task2_trie.demo import run_demo
    from src.task2_trie.homework import Homework

    run_demo()  # ассерти з умови
    # невеликий візуальний приклад
    t = Homework()
    for i, w in enumerate(["apple", "application", "banana", "bandana", "catalog", "dog", "App"]):
        t.put(w, i)

    samples = [
        ("has_prefix('app')", t.has_prefix("app")),
        ("has_prefix('APP')", t.has_prefix("APP")),
        ("count_words_with_suffix('ana')", t.count_words_with_suffix("ana")),
        ("count_words_with_suffix('og')", t.count_words_with_suffix("og")),
        ("count_words_with_suffix('App')", t.count_words_with_suffix("App")),
    ]

    print("[task2] Trie demo passed.")
    print("[task2] Showcase:")
    for k, v in samples:
        print(f"  - {k:30s} => {v}")


def run_task1() -> None:
    # Завдання 1 (Max Flow): запуск розрахунку, збереження CSV і короткий звіт
    from src.task1_maxflow.solver import run_solver

    mf, path = run_solver()
    print(f"[task1] Max flow: {mf}. CSV: {path}")

    # Додатковий «візуальний» вивід з CSV
    p = Path(path)
    if not p.exists():
        print("[task1] Увага: CSV не знайдено.")
        return

    with p.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = list(r)

    # Підсумки
    total = 0
    per_terminal = {}
    shops = set()
    for row in rows:
        flow = int(row["Flow"])
        total += flow
        shops.add(row["Shop"])
        per_terminal[row["Terminal"]] = per_terminal.get(row["Terminal"], 0) + flow

    print("[task1] Summary:")
    print(f"  - Shops served: {len(shops)} (очікуємо 14)")
    print(f"  - Total flow:   {total} (очікуємо 115)")
    for t, v in sorted(per_terminal.items()):
        print(f"  - Terminal {t}: {v}")

    # Перші 10 рядків для перегляду
    print("[task1] Sample rows (first 10):")
    print("  Terminal | Shop  | Flow")
    print("  ---------|-------|-----")
    for row in rows[:10]:
        print(f"  {row['Terminal']:<8} | {row['Shop']:<5} | {row['Flow']}")


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in {"task1", "task2"}:
        print("Usage: python main.py {task1|task2}")
        return 2

    cmd = argv[1]
    if cmd == "task1":
        run_task1()
    else:
        run_task2()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
