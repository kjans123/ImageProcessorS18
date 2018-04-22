def test_logCompression():
    from logCompression import logComp
    from base64_conv_numpy import encode_image_string as enc
    img = enc("haha.JPG")
    logCompressed_string = str(logComp(img))
    with open('testLogCompression.txt', 'r') as tester:
        testText = tester.read()
    assert logCompressed_string == testText

def test_exceptions():
    import pytest
    from logCompression import logComp
    with pytest.raises(ValueError, message="Expecting ValueError"):
        expectFail = logComp("")
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import badModule
