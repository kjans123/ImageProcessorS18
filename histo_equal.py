def histo_equal(base64String):
    """"function that takes in a base64 string, converts to img array
        and then runs a global histogram equalization process on each
        channel in the img array.

    :param base64string: takes as input a JPG base64 string from app front-end
    :returns imgArray: returns a post-processed JPG img as numpy array
    :raises ValueError: raises Value Error if base64 string is empty
    :raises ImportError: raises Import Error if numpy or scikit packages
                         are not found. Also raises Import Error if
                         base64base64_conv_numpy module is not found
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="back_end.log",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    try:
        if base64String is None or base64String == "":
            logging.warning("base64String is EMPTY")
            raise ValueError("empty base64String")
        from skimage import exposure
        import numpy as np
        try:
            from base64_conv_numpy import convert_image_to_np_array
            from base64_conv_numpy import convert_processed_np_array_to_base64
            imgArray, a_type, m, w, z = convert_image_to_np_array(base64String)
            for c in range(imgArray.shape[2]):
                imgArray[:, :, c] = exposure.equalize_hist(imgArray[:, :, c])
            # img64 = convert_processed_np_array_to_base64(imgArray)
            m = "success: processed (histo. eq.) img and returned as np array"
            logging.info(m)
            return imgArray
        except ImportError:
            msg = 'base64_conv_numpy module not found.'
            print(msg)
            logging.warning(msg)
    except ImportError:
        msgg = 'scikit/numpy packages not found. Check virtualenv'
        print(msgg)
        logging.warning(msgg)
