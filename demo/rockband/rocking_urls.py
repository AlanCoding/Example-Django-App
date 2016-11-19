from django.conf.urls import url
from rockband import views as rocking_views

urlpatterns = [
    url(r'^$', rocking_views.BandList.as_view(), name='band-list'),
    url(r'^oldest/$', rocking_views.OldestBands.as_view(), name='band-list'),
    url(r'^(?P<pk>[0-9]+)/$', rocking_views.BandDetailView.as_view(), name='band-detail'),
]
