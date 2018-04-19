from checkListOfString import check_list_of_string as chk
def test_list_of_string():
    example = ["a", "derp", "123"]
    bad = ["124", 1, "hello"]
    bad2 = "123"
    empty = [""]
    assert chk(example) == True
    assert chk(bad) == False
    assert chk(bad2) == False
    assert chk(empty) == False
