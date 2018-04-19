def test_histo_equal():
    from histo_equal import histo_equal
    from base64_conv_numpy import encode_image_string
    imageString = encode_image_string("haha.JPG")
    proc_image_string = histo_equal(imageString)
    with open('Output.txt', 'r') as testFile:
        dataString = testFile.read()
    assert str(proc_image_string) == dataString


def test_correctExcp():
    import pytest
    from histo_equal import histo_equal
    from base64_conv_numpy import encode_image_string
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = histo_equal(h)
