from django.urls import path
from . import views

urlpatterns = [
    # path('<slug:slug>', views.product_detail, name='product_detail_page'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail_page'),
]