# Create test for tmpFolderAction.py
import json
from tmpFolderAction import access_tmp, make_tmp

def test_make_tmp():
    dictionary = {
        "a": 1,
        "b": "hello",
        "c": 45.2,
        "hi": [1, 3, 2]
    }
    make_tmp(dictionary)
    with open('tmp/data.json', 'r') as f:
        data = json.load(f)
    dict_info = json.loads(data)
    assert dict_info["a"] == 1
    assert sum(dict_info["hi"]) == 6


def test_access_tmp():
    # make_tmp has been tested
    dictionary = {
        "a": 1,
        "b": "hello",
        "c": 45.2,
        "hi": [1, 3, 2]
    }
    make_tmp(dictionary)
    dict_object = access_tmp()
    assert sum(dict_object["hi"]) == 6
    assert isinstance(dict_object, dict)

# if we want to check that tmp folder exists
# as in this is not done via frontend,
# add: def test_access_no_tmp():
