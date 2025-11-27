import sys
from pathlib import Path

# Добавляем папку src в sys.path вручную
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import pytest
from lab03.text import normalize, tokenize, count_freq, top_n

#  normalize


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМиР\t", "привет мир"),
        ("Ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("   двойные  пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert (
        normalize(source) == expected
    )  # проверяем, что результат функции normalize равен ожидаемой строке


# tokenize


@pytest.mark.parametrize(
    "source, expected_tokens",
    [
        ("Привет, мир!", ["привет", "мир"]),
        ("", []),  # пустая строка
    ],
)
def test_tokenize_basic(source, expected_tokens):
    assert tokenize(source) == expected_tokens


# count_freq


def test_count_freq_basic():
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)

    assert freq["a"] == 3
    assert freq["b"] == 2
    assert freq["c"] == 1


def test_count_freq_empty():
    assert count_freq([]) == {}


# top_n


def test_top_n_basic():
    freq = {"a": 3, "b": 1, "c": 2}
    result = top_n(freq, 2)

    assert result == [("a", 3), ("c", 2)]


def test_top_n_tie_breaker():
    # одинаковая частота, значит, проверяем сортировку по алфавиту
    freq = {"banana": 2, "apple": 2, "cherry": 1}
    result = top_n(freq, 2)

    assert result == [("apple", 2), ("banana", 2)]
