from __future__ import annotations
from collections import deque, defaultdict
from typing import Dict, Tuple, List, Optional, DefaultDict

class EdmondsKarp:
    """
    Класична Edmonds–Karp на залишковій мережі.
    Зберігає матрицю потоку self.flow для подальшої декомпозиції.
    """

    def __init__(self, edges: List[Tuple[str, str, int]]) -> None:
        self.cap: DefaultDict[str, Dict[str, int]] = defaultdict(dict)
        self.flow: DefaultDict[str, Dict[str, int]] = defaultdict(dict)
        self.adj: DefaultDict[str, List[str]] = defaultdict(list)

        for u, v, c in edges:
            # акумулюємо кратні ребра
            self.cap[u][v] = self.cap[u].get(v, 0) + c
            if v not in self.adj[u]:
                self.adj[u].append(v)
            if u not in self.adj[v]:
                self.adj[v].append(u)
            self.flow[u][v] = 0
            self.flow[v].setdefault(u, 0)

    def _bfs(self, s: str, t: str) -> Tuple[int, Dict[str, Optional[str]]]:
        parent: Dict[str, Optional[str]] = {s: None}
        q = deque([(s, float("inf"))])

        while q:
            u, f = q.popleft()
            for v in self.adj[u]:
                residual = self.cap[u].get(v, 0) - self.flow[u].get(v, 0)
                if residual > 0 and v not in parent:
                    parent[v] = u
                    nf = min(f, residual)
                    if v == t:
                        return int(nf), parent
                    q.append((v, nf))
        return 0, parent

    def max_flow(self, s: str, t: str) -> int:
        total = 0
        while True:
            pushed, parent = self._bfs(s, t)
            if pushed == 0:
                break
            total += pushed
            v = t
            while v != s:
                u = parent[v]  # type: ignore[index]
                self.flow[u][v] = self.flow[u].get(v, 0) + pushed
                self.flow[v][u] = self.flow[v].get(u, 0) - pushed
                v = u  # type: ignore[assignment]
        return total
