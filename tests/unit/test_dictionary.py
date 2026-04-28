from app.dictionary.dictionary import Dictionary


def test_add_and_lookup_existing_word():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")

    result = d.Look("Apple")

    assert result == "A fruit that grows on trees"


def test_lookup_non_existing_word():
    d = Dictionary()

    result = d.Look("Banana")

    assert result == "Can't find entry for Banana"


def test_dictionary_overwrites_existing_entry():
    d = Dictionary()
    d.newentry("Apple", "A fruit")
    d.newentry("Apple", "A tech company")

    result = d.Look("Apple")

    assert result == "A tech company"
