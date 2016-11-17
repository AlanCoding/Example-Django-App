import pytest
from rockband.models import Band, Member

from django.db.models import Count

@pytest.mark.django_db
def test_invalid_instrument_choice():
    band = Band.objects.create(name='RockSugar')
    Member.objects.create(band=band, instrument='z')

@pytest.mark.django_db
def test_auto_create_by_migration():
    band = Band.objects.first()
    assert band.name == 'Rock Sugar'

@pytest.mark.django_db
def test_annotate_num_members():
    Band.objects.create(name='WeirdAl')
    qs = Band.objects.annotate(
        member_count=Count('members')
    ).order_by('-member_count')[:1]
    print qs.query
    print '\n'.join([str([band.member_count, band.name]) for band in qs.all()])
    assert False

