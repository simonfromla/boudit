from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

def shawty_redirect_view(request, *args, **kwargs):
    return HttpResponse('hey')

class ShawtyCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hey again')