def reverseVid(b64_string):
    """Function that inputs one base64 string and processes
       via Reverse Video. Outputs the processed base64 string

    :param b64_string: base 64 pre-processed image string
    :returns post_b64: base 64 post-processed image string
    :raises ImportError: raises error if skimage or base64_conv_numpy.py not found
    :raises ValueError: raises error if the input string is empty
    """
    import logging
    logging.basicConfig(filename="back_end.log",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    if b64_string == "" or b64_string is None:
        logging.warning("Empty input given. Please provide base64 string")
        raise ValueError("No base64 string")
    try:
        from base64_conv_numpy import convert_image_to_np_array, convert_processed_np_array_to_base64
        from skimage import util
        import numpy as np
    except ImportError:
        note = "Packages from numpy, scikit, and base64_conv_numpy.py not found"
        print(note)
        logging.warning(note)
    array, a_type, m, w, z = convert_image_to_np_array(b64_string)
    logging.info("Convert b64 to numpy array")
    # data is in here and subtract each thing from 1
    one_matrix = np.ones(array.shape)
    inverted = one_matrix - array
    logging.info("Numpy array processed by Reverse Video")
    post_b64 = convert_processed_np_array_to_base64(inverted)
    logging.info("Processed array converted back to base64")
    return post_b64
