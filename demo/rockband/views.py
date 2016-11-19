from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.db.models import Avg
from django.shortcuts import get_object_or_404

from rockband import models

## -- Old function-style views --
def band_listing(request):
    """A view of all bands."""
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    bands = models.Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})


# def band_detail(request, d):
#     band = get_object_or_404(Band, pk=d)
#     return render(request, 'bands/band_detail.html', {'band': band})


def raise_exception(request):
    raise Exception()


class BandDetailView(DetailView):

    context_object_name = 'band'
    template_name = 'bands/band_detail.html'
    model = models.Band

class OldestBands(ListView):

    context_object_name = 'bands'
    template_name = 'bands/band_listing.html'
    queryset = models.Band.objects.annotate(
        average_age=Avg('members__age')
    ).order_by('-average_age')

    paginate_by = 2

