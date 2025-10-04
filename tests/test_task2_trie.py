import os
import sys

# Додаємо корінь проєкту в sys.path, щоб імпорт працював при запуску з різних робочих директорій
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.task2_trie.homework import Homework  # noqa: E402


def build_trie():
    t = Homework()
    words = [
        "apple", "application", "banana", "band", "bandana",
        "cat", "catalog", "dog", "dodge", "App"  # перевірка регістру
    ]
    for i, w in enumerate(words):
        t.put(w, i)
    return t


def test_has_prefix_positive_negative():
    t = build_trie()
    assert t.has_prefix("app") is True      # apple, application
    assert t.has_prefix("ban") is True      # banana, band, bandana
    assert t.has_prefix("cat") is True      # cat, catalog
    assert t.has_prefix("do") is True       # dog, dodge
    assert t.has_prefix("App") is True      # слово з великої літери
    assert t.has_prefix("APP") is False     # регістр враховується
    assert t.has_prefix("zzz") is False


def test_count_words_with_suffix_basic():
    t = build_trie()
    assert t.count_words_with_suffix("e") == 2    # apple, dodge
    assert t.count_words_with_suffix("ana") == 2  # banana, bandana
    assert t.count_words_with_suffix("og") == 2   # catalog, dog
    assert t.count_words_with_suffix("d") == 1    # band
    assert t.count_words_with_suffix("App") == 1  # рівно "App"
    assert t.count_words_with_suffix("pp") == 1   # App


def test_invalid_inputs():
    t = build_trie()
    import pytest
    with pytest.raises(ValueError):
        t.has_prefix("")
    with pytest.raises(ValueError):
        t.count_words_with_suffix("")

    for val in (None, 123, 4.56, ["a"], {"x": 1}):
        with pytest.raises(TypeError):
            t.has_prefix(val)  # type: ignore[arg-type]
        with pytest.raises(TypeError):
            t.count_words_with_suffix(val)  # type: ignore[arg-type]
