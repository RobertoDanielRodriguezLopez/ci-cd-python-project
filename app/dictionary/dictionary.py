from typing import Dict


class Dictionary:
    def __init__(self) -> None:
        self.dictionary: Dict[str, str] = {}

    def newentry(self, word: str, definition: str) -> None:
        self.dictionary[word] = definition

    def Look(self, word: str) -> str:
        if word in self.dictionary:
            return self.dictionary[word]
        return f"Can't find entry for {word}"
