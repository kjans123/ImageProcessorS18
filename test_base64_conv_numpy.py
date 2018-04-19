def test_base64base64_conv_numpy():
    from base64_conv_numpy import convert_image_to_np_array
    from base64_conv_numpy import convert_processed_np_array_to_base64
    from base64_conv_numpy import encode_image_string
    import numpy as np
    imgString = encode_image_string('haha.JPG')
    a, a_type, m, w, z = convert_image_to_np_array(imgString)
    assert str(a_type) == 'uint8'
    assert a[9, 10, 2] == 13
    assert a[1, 1, 1] == 17
    assert a[3569, 5290, 2] == 9
    assert m == 3570
    assert w == 5291
    assert z == 3
    with open('testString.txt', 'r') as testFile:
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
