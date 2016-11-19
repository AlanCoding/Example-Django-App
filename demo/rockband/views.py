from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.db.models import Avg
# from django.shortcuts import get_object_or_404

from rockband import models

## -- Old function-style views --
# def band_listing(request):
#     """A view of all bands."""
#     print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
#     bands = models.Band.objects.all()
#     return render(request, 'bands/band_listing.html', {'bands': bands})


# def band_detail(request, d):
#     band = get_object_or_404(Band, pk=d)
#     return render(request, 'bands/band_detail.html', {'band': band})

class BandListView(ListView):


    def get_queryset(self):
        """
        Allow for filtering bands based on whether the querystring 'name'
        occurs in the band's name.
        example pattern: http://bandapp.com/bands/?name=quartet
        """
        qs = super(BandListView, self).get_queryset()
        name = self.request.GET.get('name', None)
        if name:
            qs = qs.filter(name__icontains=name)
        return qs

    def get_paginate_by(self, queryset, *args, **kwargs):
        """
        Allow for custom pagination based on URL in querystring
        example pattern: http://bandapp.com/bands/?paginate_by=2&page=2
        """
        page_size = self.request.GET.get('paginate_by', None)
        if not page_size:
            page_size = super(BandListView, self).get_paginate_by(queryset)
        return page_size


class BandDetailView(DetailView):

    context_object_name = 'band'
    template_name = 'bands/band_detail.html'
    model = models.Band


class BandList(BandListView):

    model = models.Band
    context_object_name = 'bands'
    template_name = 'bands/band_listing.html'


class OldestBands(BandListView):

    context_object_name = 'bands'
    template_name = 'bands/band_listing.html'
    queryset = models.Band.objects.annotate(
        average_age=Avg('members__age')
    ).order_by('-average_age')

    paginate_by = 2

