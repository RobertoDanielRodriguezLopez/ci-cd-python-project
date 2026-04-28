def build_word(words: list[str]) -> str:
    """
    Build a new word by taking the n-th character of the n-th word.
    """
    result = []

    for index, word in enumerate(words):
        result.append(word[index])

    return "".join(result)
