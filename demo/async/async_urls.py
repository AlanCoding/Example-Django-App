from django.conf.urls import url
from async import views

urlpatterns = [
    url(r'^slow/$', views.slow_page, name='long-wait'),
    url(r'^fast/$', views.fast_page, name='threaded'),
]
