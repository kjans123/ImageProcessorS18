def bytes_to_string(bytes_object):
    """"function that removes b' and final ' from
        bytes object

    :param bytes_object: takes as input bytes base64 object
    :returns: strBytes: returns bytes object as string with
              leading b' and final ' removed
    """
    import logging
    str1 = logging.DEBUG
    logging.basicConfig(filename="back_end.log",
                        format='%(levelname)s %(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
    strBytes = str(bytes_object)
    strBytes = strBytes[2:]
    strBytes = strBytes[:-1]
    logging.info("success: trimmed bytes object")
    return strBytes
