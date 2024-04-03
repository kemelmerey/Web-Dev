from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Products, Category
# Create your views here.

#categories, category_detail, products, product_detail, category_products
def categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(category.to_json())

def products(request):
    products = Products.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def product_detail(request, id):
    try:
        product = Products.objects.get(id=id)
    except Products.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse(product.to_json())

def category_products(request, id):
    category = Category.objects.get(id = id)
    products = Products.objects.filter(category = category)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe = False)