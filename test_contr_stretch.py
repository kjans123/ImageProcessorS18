def test_contr_stretch():
    from contr_strech import contr_stretch
    from base64_conv_numpy import encode_image_string
    import numpy as np
    imageString = encode_image_string("haha.JPG")
    proc_image_Array = contr_stretch(imageString)
    dataArray = np.load('contr_array.txt.npy')
    assert proc_image_Array.all() == dataArray.all()


def test_correctExcp():
    import pytest
    from contr_strech import contr_stretch
    from base64_conv_numpy import encode_image_string
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = contr_stretch(h)
