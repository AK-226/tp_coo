from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Departement

# Create your views here.

class DepartementDetailView(DetailView):
    model = Departement
    def render_to_response(self, context, **response_kwargs):
        return HttpsResponse(dumps(self.object.json()))
