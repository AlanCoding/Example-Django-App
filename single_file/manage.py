import sys

from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse


settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse('Hello World')


def echo(request, val):
    print val
    return HttpResponse('Your URL contained: ' + str(val))


urlpatterns = (
    url(r'^$', index),
    url(r'^(?P<val>[a-z]+)/$', echo),
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)