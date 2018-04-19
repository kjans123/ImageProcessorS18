def histo_equal(base64String):
    from skimage.util import img_as_ubyte
    from skimage import exposure
    from skimage.morphology import disk
    from skimage.filters import rank
    import numpy as np
    import base64
    from base64_conv_numpy import convert_image_to_np_array
    from base64_conv_numpy import convert_processed_np_array_to_base64
    from base64_conv_numpy import encode_image_string
    imgArray, a_type, m, w, z = convert_image_to_np_array(base64String)
    for channel in range(imgArray.shape[2]):
        imgArray[:, :, channel] = exposure.equalize_hist(imgArray[:, :, channel])
    print(imgArray.dtype)
    return imgArray
