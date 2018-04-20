def test_contr_stretch():
    from contr_strech import contr_stretch
    from base64_conv_numpy import encode_image_string
    imageString = encode_image_string("haha.JPG")
    proc_image_string = contr_stretch(imageString)
    with open('Output2.txt', 'r') as testFile:
        dataString = testFile.read()
    assert str(proc_image_string) == dataString


def test_correctExcp():
    import pytest
    from contr_strech import contr_stretch
    from base64_conv_numpy import encode_image_string
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = contr_stretch(h)
