def test_reverseVid():
    from reverseVideo import reverseVid
    from base64_conv_numpy import encode_image_string as enc
    img = enc("haha.JPG")
    inverted_string = str(reverseVid(img))
    with open('testInvert.txt', 'r') as tester:
        testText = tester.read()
    assert inverted_string == testText

def test_exceptions():
    import pytest
    from reverseVideo import reverseVid
    with pytest.raises(ValueError, message="Expecting ValueError"):
        expectFail = reverseVid("")
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import badModule
