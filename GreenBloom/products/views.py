from django.shortcuts import render
from .forms import FilterForm
from .models import Product
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def list_products(request):
    products = Product.objects.all()
    if request.method == "POST":
        filterSearch = FilterForm(request.POST)
        if filterSearch.is_valid():
            category = filterSearch.cleaned_data.get('category')

            if category == 'ALL':
                filterProduct = Product.objects.all()
            else:
                filterProduct = products.filter(category=category)

            context = {
                "filterSearch" : filterSearch,
                "filterProduct" : filterProduct,
                "is_filter" : True,
            }
            return render(request, 'products.html', context)
    else:
        filterSearch = FilterForm()
        context = {
            "filterSearch" : filterSearch,
            "products" : products,
            "is_filter" : False,
        }
    return render(request, 'products.html', context)