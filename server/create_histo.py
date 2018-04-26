def create_histo(npArray):
    """"function that takes in a numpy array and creates a histogram
        matplotlib plot. Saves as jpg and converts to base64 string.

    :param npArray: takes as as input a numpy image array
    :returns img64: returns a histogram plot as base64 string
    :raises ValueError: raises Value Error if numpy array is empty
    :raises ValueError: raises Value Error if numpy array 3rd dim
                        is not 3
    :raises KeyError: raises Key Error if input array does not have
                      have a third dimension
    :raises ImportError: raises Import Error if numpy,
                         scikit, os, or matplotlib packages
                         are not found. Also raises Import Error if
                         base64base64_conv_numpy module is not found.
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="back_end.log",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        import matplotlib
        import os
        try:
            from base64_conv_numpy import encode_image_string
            fig, ax = plt.subplots()
            h = np.array([])
            if (npArray is None or npArray.all() == h or
                    npArray.size == 0):
                logging.warning("numpy array is EMPTY")
                raise ValueError("empty numpy array")
            try:
                if npArray.shape[2] != 3:
                    logging.warning("numpy array third dimension must be 3")
                    raise ValueError("numpy array third dimension must be 3")
            except IndexError:
                print("input array must have a 3rd dimensions")
                logging.warning("input array does not have a 3rd dimension")
                raise IndexError("input array must have 3 dimensions")
            c = 256
            n, bins, patches = ax.hist(npArray.ravel(), c, color='blue')
            ax.plot(bins)
            ax.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
            ax.set_xlabel('Pixel intensity')
            ax.set_xlim(0, 1)
            fig.tight_layout()
            plt.savefig('tempPlot.jpg')
            img64 = encode_image_string('tempPlot.jpg')
            os.remove('tempPlot.jpg')
            logging.info("success: histogram base64 string created")
            return img64
        except ImportError:
            msg = 'base64_conv_numpy module not found.'
            print(msg)
            logging.warning(msg)
    except ImportError:
        msgg = 'scikit/numpy/matplotlib packages not found. Check virtualenv'
        print(msgg)
        logging.warning(msgg)
