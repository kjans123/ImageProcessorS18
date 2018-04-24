def test_base64_conv_numpy():
    from base64_conv_numpy import convert_image_to_np_array
    from base64_conv_numpy import convert_processed_np_array_to_base64
    from base64_conv_numpy import encode_image_string
    import numpy as np
    imgString = encode_image_string('tiny.jpg')
    a, a_type, m, w, z = convert_image_to_np_array(imgString)
    assert str(a_type) == 'float64'
    assert a[9, 10, 2] == 0.08627450980392157
    assert a[1, 1, 1] == 0
    assert a[647, 1151, 2] == 0.08627450980392157
    assert m == 648
    assert w == 1152
    assert z == 3
    with open('base64_test.txt', 'r') as testFile:
        dataString = testFile.read()
    img64 = convert_processed_np_array_to_base64(a)
    assert str(img64) == dataString


def test_correctExcp():
    from base64_conv_numpy import convert_image_to_np_array
    from base64_conv_numpy import convert_processed_np_array_to_base64
    from base64_conv_numpy import encode_image_string
    import numpy as np
    import pytest
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = convert_image_to_np_array(h)
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = convert_processed_np_array_to_base64(h)
