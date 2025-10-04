from __future__ import annotations
import sys


def run_task2() -> None:
    # Демонстрація для Trie (Завдання 2)
    from src.task2_trie.demo import run_demo

    run_demo()
    print("[task2] Trie demo passed.")


def run_task1() -> None:
    # Плейсхолдер на майбутнє (щоб програма не падала)
    try:
        from src.task1_maxflow.solver import run_solver  # noqa: F401
    except Exception:
        print("[task1] Ще не реалізовано. Повернемось після завершення Завдання 2.")
        return
    # Якщо ти вже додав solver — можеш розкоментити нижче:
    # mf, path = run_solver()
    # print(f"[task1] Max flow: {mf}. CSV: {path}")


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in {"task1", "task2"}:
        print("Usage: python main.py {task1|task2}")
        return 2

    cmd = argv[1]
    if cmd == "task2":
        run_task2()
    else:
        run_task1()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
