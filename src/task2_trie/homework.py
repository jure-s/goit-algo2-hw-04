from __future__ import annotations
from typing import Any
from .trie import Trie


class Homework(Trie):
    """
    Розширення Trie двома методами з умови:
    - count_words_with_suffix(pattern) -> int
    - has_prefix(prefix) -> bool

    Валідація:
      * параметри мають бути рядками;
      * порожній рядок вважаємо некоректним (ValueError) — так ми явно
        змушуємо студента задавати осмислені шаблони/префікси.
    """

    # Внутрішній валідатор для параметрів завдання
    def _ensure_str_param(self, value: Any, name: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string")
        if value == "":
            raise ValueError(f"{name} must be a non-empty string")
        return value

    def count_words_with_suffix(self, pattern) -> int:
        pattern = self._ensure_str_param(pattern, "pattern")
        # Ефективність: одне повне проходження по trie (лінійне від кількості символів збережених слів)
        # без додаткових структур і перетворень регістру.
        return sum(1 for w in self.iter_words() if w.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        prefix = self._ensure_str_param(prefix, "prefix")
        # Якщо шлях у trie за цим префіксом існує — гарантовано існує хоча б одне слово,
        # оскільки вузли створюються лише під час вставки дійсних слів.
        return self._traverse(prefix) is not None
