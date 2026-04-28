class Dictionary:
    def __init__(self):
        self._entries = {}

    def newentry(self, word: str, definition: str) -> None:
        """
        Add a new word and its definition to the dictionary.
        """
        self._entries[word] = definition

    def Look(self, word: str) -> str:
        """
        Retrieve a definition for the given word.
        """
        if word in self._entries:
            return self._entries[word]
        return f"Can't find entry for {word}"
