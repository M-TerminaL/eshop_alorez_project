from django.urls import path
from . import views

urlpatterns = [
    # main addr
    path('categories/', views.product_list, name='product_list_page'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail_page'),
    # api addr
    path('api/generics/<slug:slug>', views.ProductDetailGenericApiView.as_view(), name='api_product_detail_page')

]