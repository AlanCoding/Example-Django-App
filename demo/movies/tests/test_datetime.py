import pytest
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
    rating = Rating(timestamp=raw_time)
    rating.save()
    assert rating.timestamp is not None
