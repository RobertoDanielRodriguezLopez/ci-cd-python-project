from app.dictionary.dictionary import Dictionary


def test_add_and_lookup_existing_word():
    d = Dictionary()
    d.add_entry("Apple", "A fruit that grows on trees")

    result = d.lookup("Apple")
    assert result == "A fruit that grows on trees"


def test_lookup_non_existing_word():
    d = Dictionary()

    result = d.lookup("Banana")
    assert result is None


def test_dictionary_overwrites_existing_entry():
    d = Dictionary()
    d.add_entry("Apple", "A fruit")
    d.add_entry("Apple", "A tech company")

    result = d.lookup("Apple")
    assert result == "A tech company"


def test_dictionary_is_case_insensitive():
    d = Dictionary()
    d.add_entry("Apple", "a fruit")

    assert d.lookup("apple") == "a fruit"
    assert d.lookup("APPLE") == "a fruit"
    assert d.lookup("ApPlE") == "a fruit"
