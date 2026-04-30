from typing import List


def build_word(words: List[str]) -> str:
    result = ""

    for index, word in enumerate(words):
        if len(word) > index:
            result += word[index]

    return result
