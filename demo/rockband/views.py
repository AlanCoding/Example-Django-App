from django.shortcuts import render
from rockband import models

# Create your views here.

def band_listing(request):
    """A view of all bands."""
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    bands = models.Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})

def raise_exception(request):
    raise Exception()

def band_detail(request, d):
    band = models.Band.objects.get(pk=d)
    return render(request, 'bands/band_detail.html', {'band': band})

