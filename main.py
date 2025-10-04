from __future__ import annotations
import sys


def run_task2() -> None:
    # Завдання 2 (Trie): демо з assert'ами
    from src.task2_trie.demo import run_demo

    run_demo()
    print("[task2] Trie demo passed.")


def run_task1() -> None:
    # Завдання 1 (Max Flow): запуск розрахунку та збереження CSV
    from src.task1_maxflow.solver import run_solver

    mf, path = run_solver()
    print(f"[task1] Max flow: {mf}. CSV: {path}")


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
