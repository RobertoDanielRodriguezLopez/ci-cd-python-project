from typing import Dict


class Dictionary:
    def __init__(self) -> None:
        self.entries: Dict[str, str] = {}

    def newentry(self, word: str, definition: str) -> None:
        self.entries[word] = definition

    def look(self, word: str) -> str:
        if word in self.entries:
            return self.entries[word]
        return f"Can't find entry for {word}"
