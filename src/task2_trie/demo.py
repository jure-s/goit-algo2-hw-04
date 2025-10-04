from .homework import Homework

def run_demo() -> None:
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка суфіксів (з умови)
    assert trie.count_words_with_suffix("e") == 1   # apple
    assert trie.count_words_with_suffix("ion") == 1 # application
    assert trie.count_words_with_suffix("a") == 1   # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Перевірка префіксів (з умови)
    assert trie.has_prefix("app") is True
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True
    assert trie.has_prefix("ca") is True

if __name__ == "__main__":
    run_demo()
    print("Demo passed.")
