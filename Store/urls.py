from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.allProducts, name="all_products"),
    path('item/<slug:slug>/', views.productDetail, name="product_detail"),
    path('search/<slug:category_slug>/', views.categoryList, name="category_list"),
]
