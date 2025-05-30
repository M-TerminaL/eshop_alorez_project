from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Product
from rest_framework import generics
from .serializers import ProductDetailSerializer


# Create your views here.

# ----
# Method A
# use function base view for product detail view page
# ----
def product_detail(request: HttpRequest, slug):
    # try:
    #     product = Product.objects.get(url_title=slug, is_active=True, is_delete=False)
    # except:
    #     raise Http404
    product = get_object_or_404(Product, url_title=slug, is_active=True, is_delete=False)
    context = {
        'product': product
    }
    return render(request, 'product_module/product_detail.html', context)


# ----
# Method B
# use Class Base view for product detail view page
# ----
class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_queryset(self):
        base_query = super().get_queryset()
        filtered_data = base_query.filter(is_active=True, is_delete=False)
        return filtered_data


# ----
# use Api view for product detail view page
# ----

class ProductDetailGenericApiView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True, is_delete=False)
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
