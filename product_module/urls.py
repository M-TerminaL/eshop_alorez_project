from django.urls import path
from . import views

urlpatterns = [
    # main
    # path('<slug:slug>', views.product_detail, name='product_detail_page'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail_page'),
    # api
    path('api/generics/<slug:slug>', views.ProductDetailGenericApiView.as_view(), name='api_product_detail_page')
]