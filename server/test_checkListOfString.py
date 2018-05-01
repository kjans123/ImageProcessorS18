def test_list_of_string():
    from checkListOfString import check_list_of_string as chk
    example = ["a", "derp", "123"]
    bad = ["124", 1, "hello"]
    bad2 = "123"
    empty = [""]
    assert chk(example) is True
    assert chk(bad) is False
    assert chk(bad2) is False
    assert chk(empty) is False
