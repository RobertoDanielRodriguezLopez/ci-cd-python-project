from typing import Dict


class Dictionary:
    def __init__(self) -> None:
        self.entries: Dict[str, str] = {}

    def newentry(self, word: str, definition: str) -> None:
        normalized_word = word.lower()
        self.entries[normalized_word] = definition

    def look(self, word: str) -> str:
        normalized_word = word.lower()
        if normalized_word in self.entries:
            return self.entries[normalized_word]
        return f"Can't find entry for {word}"
