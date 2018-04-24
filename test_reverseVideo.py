def test_reverseVid():
    from reverseVideo import reverseVid
    from base64_conv_numpy import encode_image_string as enco
    import numpy as np
    img = enco("tiny.jpg")
    dataArray = np.load('rev_test.npy')
    reveVid_array = reverseVid(img)
    assert reveVid_array.all() == dataArray.all()


def test_exceptions():
    import pytest
    from reverseVideo import reverseVid
    with pytest.raises(ValueError, message="Expecting ValueError"):
        expectFail = reverseVid("")
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import badModule
