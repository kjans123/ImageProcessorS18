def getHeader(ext=".jpg"):
    header_dict = {".png": "data:image/png;base64,",
                   ".jpg": "data:image/jpeg;base64,",
                   ".tif": "data:image/tiff;base64,",
                   ".zip": "data:application/zip;base64,"}
    return header_dict[ext]
