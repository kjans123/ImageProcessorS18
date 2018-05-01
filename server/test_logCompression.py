def test_logCompression():
    from logCompression import logComp
    from base64_conv_numpy import encode_image_string as enco
    import numpy as np
    img = enco("tiny.jpg")
    logCompressed_array = logComp(img)
    dataArray = np.load('log_test.npy')
    assert dataArray.all() == logCompressed_array.all()


def test_exceptions():
    import pytest
    from logCompression import logComp
    with pytest.raises(ValueError, message="Expecting ValueError"):
        expectFail = logComp("")
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import badModule
