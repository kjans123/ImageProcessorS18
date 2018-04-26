def test_create_histo():
    import pytest
    from base64_conv_numpy import encode_image_string
    from base64_conv_numpy import convert_image_to_np_array
    from create_histo import create_histo
    import numpy as np
    with pytest.raises(ImportError, message="Expecting ImportError"):
        import randomFunc
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = None
        e = create_histo(h)
    with pytest.raises(ValueError, message="Expecting ValueError"):
        h = np.arange(20).reshape((4, 2, 2))
    with pytest.raises(IndexError, message="Expecting IndexError"):
        h = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 6, 7]])
        e = create_histo(h)
