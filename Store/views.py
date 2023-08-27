from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def allProducts(request):
    products = Product.objects.all()
    return render(request, 'Store/home.html', {'products':products})

def productDetail(request, slug):
    product = get_object_or_404(Product, slug=slug, inStock=True)
    return render(request, 'Store/products/detail.html', {'product':product})

def categoryList(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'Store/products/category.html', {'category':category, 'products': products})