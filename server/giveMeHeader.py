def getHeader(ext=".jpg"):
    """"short function that takes as input file
        ext from front end and returns the appropriate
        header to return to front end

    :param ext: takes as input file extension
    :returns header_dict[ext]: returns the appropriate value
                               from the header_dict dictionary
                               based on the passed ext key
    """
    header_dict = {".png": "data:image/png;base64,",
                   ".jpg": "data:image/jpeg;base64,",
                   ".tif": "data:image/tiff;base64,",
                   ".zip": "data:application/zip;base64,"}
    return header_dict[ext]
