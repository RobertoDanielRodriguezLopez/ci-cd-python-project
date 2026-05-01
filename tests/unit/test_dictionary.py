from app.dictionary.dictionary import Dictionary


def test_add_and_lookup_existing_word():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")

    result = d.look("Apple")
    assert result == "A fruit that grows on trees"


def test_lookup_non_existing_word():
    d = Dictionary()

    result = d.look("Banana")
    assert result == "Can't find entry for Banana"


def test_dictionary_overwrites_existing_entry():
    d = Dictionary()
    d.newentry("Apple", "A fruit")
    d.newentry("Apple", "A tech company")

    result = d.look("Apple")
    assert result == "A tech company"


def test_dictionary_is_case_insensitive():
    d = Dictionary()
    d.newentry("Apple", "a fruit")

    assert d.look("apple") == "a fruit"
    assert d.look("APPLE") == "a fruit"
    assert d.look("ApPlE") == "a fruit"
