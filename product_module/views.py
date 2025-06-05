from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Product, ProductComment
from rest_framework import generics
from .serializers import ProductDetailSerializer


# Create your views here.


# use function base view for product detail view page (Method A)
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

# use Class Base view for product detail view page ( Used This Method in urls ) (Method B)
class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        main_product_comments = ProductComment.objects.filter(product__slug=slug, status='PB',
                                                              parent=None).prefetch_related('productcomment_set')
        context['main_product_comments'] = main_product_comments
        return context

    def get_queryset(self):
        base_query = super().get_queryset()
        filtered_data = base_query.filter(is_active=True, is_delete=False)
        return filtered_data


# ----

# use Api view for product detail view page
class ProductDetailGenericApiView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True, is_delete=False)
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'


# ----
# use function base view for products list page
def product_list(request):
    products = Product.objects.filter(is_active=True, is_delete=False)
    context = {
        'products': products
    }
    return render(request, 'product_module/product_list.html', context)


# ----
# use Class base view for products list page ( Method B ) (used this way in urls)
class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = 9
# ----
