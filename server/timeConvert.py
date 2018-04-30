import datetime


def time2str(dt):
    """Function that converts datetime object to string

    :param dt: datetime object
    :raises TypeError: error raised if input is not datetime object
    :returns timeString: returns the converted datetime string
    """
    now = datetime.datetime.now()
    if (isinstance(dt, type(now)) is True or
       isinstance(dt, datetime.timedelta) is True):
        return dt.isoformat()
    else:
        raise TypeError("Please provide datetime object!")


def str2time(strtime):
    """Function that converts string to datetime object

    :param strtime: datetime string
    :raises TypeError: raised if input is not a string
    :returns dt: returns the converted datetime object
    """
    if isinstance(strtime, str) is False:
        raise TypeError("Please provide a string!")
    dt = datetime.datetime.strptime(strtime, "%Y-%m-%dT%H:%M:%S.%f")
    return dt
