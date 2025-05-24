from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.

def index_page(request):
    return render(request, 'home_module/index.html')


def site_header_component(request: HttpRequest):
    return render(request, 'shared/site_header_component.html')


def site_footer_component(request: HttpRequest):
    return render(request, 'shared/site_footer_component.html')
