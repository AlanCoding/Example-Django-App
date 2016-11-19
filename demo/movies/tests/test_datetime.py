import pytest
from datetime import datetime
from movies.models import Rating

raw_time = 878887116
raw_time_str = '878887116'


@pytest.mark.django_db
def test_raw_time():
    rating = Rating(raw_time=raw_time)
    rating.save()
    assert rating.raw_time == raw_time

@pytest.mark.django_db
def test_formatted_time():
    # From Josiah
    dt = datetime.fromtimestamp(
        float(raw_time_str)).strftime("%Y-%m-%d %H:%M")
    rating = Rating(timestamp=dt)
    rating.save()
    print (' timestamp ' + str(rating.timestamp))
    assert rating.timestamp is not None
