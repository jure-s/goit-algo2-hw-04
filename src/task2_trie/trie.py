from __future__ import annotations
from typing import Any, Dict, Generator, Optional


class _Node:
    __slots__ = ("children", "is_end", "value")

    def __init__(self) -> None:
        self.children: Dict[str, _Node] = {}
        self.is_end: bool = False
        self.value: Optional[Any] = None


class Trie:
    """
    Базове префіксне дерево з методами put/get/contains та ітерацією по збережених словах.
    Регістр символів зберігається без змін (враховується у всіх перевірках).
    """

    def __init__(self) -> None:
        self._root = _Node()
        self._size = 0  # кількість збережених ключів

    # --------- Внутрішні допоміжні ---------
    def _ensure_str_key(self, key: Any, *, empty_ok: bool = False) -> str:
        if not isinstance(key, str):
            raise TypeError("key must be a string")
        if not empty_ok and key == "":
            raise ValueError("key must be a non-empty string")
        return key

    def _traverse(self, prefix: str) -> Optional[_Node]:
        node = self._root
        for ch in prefix:
            nxt = node.children.get(ch)
            if nxt is None:
                return None
            node = nxt
        return node

    def _iter_words_from(self, node: _Node, prefix: str) -> Generator[str, None, None]:
        if node.is_end:
            yield prefix
        for ch, nxt in node.children.items():
            yield from self._iter_words_from(nxt, prefix + ch)

    # --------- Публічні методи ---------
    def put(self, key: Any, value: Any) -> None:
        key = self._ensure_str_key(key)
        node = self._root
        for ch in key:
            node = node.children.setdefault(ch, _Node())
        if not node.is_end:
            self._size += 1
        node.is_end = True
        node.value = value

    def get(self, key: Any, default: Any = None) -> Any:
        key = self._ensure_str_key(key)
        node = self._traverse(key)
        if node is not None and node.is_end:
            return node.value
        return default

    def contains(self, key: Any) -> bool:
        key = self._ensure_str_key(key)
        node = self._traverse(key)
        return bool(node and node.is_end)

    def iter_words(self) -> Generator[str, None, None]:
        """Повертає усі збережені слова (ключі)."""
        yield from self._iter_words_from(self._root, "")

    def __len__(self) -> int:
        return self._size
