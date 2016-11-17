import pytest
from rockband.models import Band, Member

@pytest.mark.django_db
def test_invalid_instrument_choice():
    band = Band.objects.create(name='RockSugar')
    Member.objects.create(band=band, instrument='z')

@pytest.mark.django_db
def test_auto_create_by_migration():
    band = Band.objects.first()
    assert band.name == 'Rock Sugar'
