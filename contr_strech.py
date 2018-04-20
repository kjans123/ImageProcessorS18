def contr_stretch(base64String):
    """"function that intakes an image as base64 string. Converts to np
        array and runs contrast stretching on array. Returns image as
        base64 string. For min and max of contrast stretching, takes
        values in 40th and 95th percentile respectively.

    :param base64string: takes as input a JPG base64 string from app front-end
    :returns imgString: returns a post-processed JPG img as base64 string
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
        from skimage import exposure
        import numpy as np
        try:
            from base64_conv_numpy import convert_image_to_np_array
            from base64_conv_numpy import convert_processed_np_array_to_base64
            if base64String is None or base64String == "":
                logging.warning("base64String is EMPTY")
                raise ValueError("empty base64String")
            imgArray, a_type, m, w, z = convert_image_to_np_array(base64String)
            v1, v2 = np.percentile(imgArray, (0.4, 95))
            imgC = exposure.rescale_intensity(imgArray, in_range=(v1, v2))
            imgString = convert_processed_np_array_to_base64(imgC)
            print(imgString)
            m = "success: processed (contr. str.) img and returned as base64"
            logging.info(m)
            return imgString
        except ImportError:
            msg = 'base64_conv_numpy module not found.'
            print(msg)
            logging.warning(msg)
    except ImportError:
        msgg = 'scikit/numpy packages not found. Check virtualenv'
        print(msgg)
        logging.warning(msgg)
