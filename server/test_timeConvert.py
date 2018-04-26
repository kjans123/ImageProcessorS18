import datetime
from timeConvert import str2time, time2str


def test_conversion():
    dt = datetime.datetime.now()
    string = time2str(dt)
    # time2str(dt) is actually just dt.isoformat()
    # a pre-made function from datetime
    assert dt == str2time(string)


def test_exceptions():
    import pytest
    with pytest.raises(TypeError, message="Expecting AttributeError"):
        ex = time2str(3)
    with pytest.raises(TypeError, message="Expecting TypeError"):
        ex = str2time(4)
