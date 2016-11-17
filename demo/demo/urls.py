"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
import debug_toolbar

from rockband import views as rocking_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', admin.site.urls),
    # Rock band urls
    url(r'^bands/$', rocking_views.band_listing, name='band-list'),
    url(r'^exception/$', rocking_views.raise_exception),
    url(r'^bands/(\d+)/$', rocking_views.band_detail, name='band-detail'),
    # url(r'^bands/search/$', rocking_views.band_search, name='band-search'),
    # url(r'$mv/', mo)
]

# For the debug toolbar
if settings.DEBUG:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
