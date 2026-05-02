from typing import Dict, Optional
 
 
class Dictionary:
    def __init__(self) -> None:
        self.entries: Dict[str, str] = {}
 
    def add_entry(self, word: str, definition: str) -> None:
        normalized_word = word.lower()
        self.entries[normalized_word] = definition
 
    def lookup(self, word: str) -> Optional[str]:
        normalized_word = word.lower()
        return self.entries.get(normalized_word)
