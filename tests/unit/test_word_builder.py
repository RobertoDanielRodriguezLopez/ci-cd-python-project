from app.words.word_builder import build_word


def test_build_word_basic_case():
    words = ["yoda", "best", "has"]

    result = build_word(words)

    assert result == "yes"


def test_build_word_single_word():
    words = ["hello"]

    result = build_word(words)

    assert result == "h"


def test_build_word_empty_list():
    words = []

    result = build_word(words)

    assert result == ""
