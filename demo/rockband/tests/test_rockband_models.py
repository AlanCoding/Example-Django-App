import pytest
from rockband.models import Band, Member

from django.db.models import Count, Avg, Sum

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
    qs = Band.objects.annotate(
        member_count=Count('members')
    ).order_by('-member_count')[:1]
    print '\n'.join([str([band.member_count, band.name]) for band in qs.all()])
    assert qs.all()[0].member_count == 2  # Largest band has 2 members

@pytest.mark.django_db
def test_aggregate_members():
    band = Band.objects.get(name='Rock Sugar')
    assert band.members.count() == 2

@pytest.mark.django_db
def test_band_order_avg_age():
    band = Band.objects.get(name='Rock Sugar')
    agg_qs = band.members.aggregate(
        average_age=Avg('age')
    )
    print agg_qs
    assert agg_qs['average_age'] == 50.5
    assert band.average_member_age == 50.5

@pytest.mark.django_db
def test_order_by_avg_age():
    qs = Band.objects.annotate(
        average_age=Avg('members__age')
    ).order_by('-average_age')
    print [band.average_age for band in qs.all()]
    assert qs.all()[0].average_age == 50.5
