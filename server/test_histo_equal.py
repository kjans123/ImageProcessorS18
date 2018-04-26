def test_histo_equal():
    from histo_equal import histo_equal
    from base64_conv_numpy import encode_image_string
    import numpy as np
    imageString = encode_image_string("tiny.jpg")
    proc_image_Array = histo_equal(imageString)
    dataArray = np.load('hist_test.npy')
    assert proc_image_Array.all() == dataArray.all()


def test_correctExcp():
    import pytest
    from histo_equal import histo_equal
    from base64_conv_numpy import encode_image_string
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = histo_equal(h)
