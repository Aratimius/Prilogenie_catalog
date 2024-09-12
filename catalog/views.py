from django.shortcuts import render
from catalog.models import Product


def home(request):
    """Контроллер отображения главной страницы"""
    last_products = Product.objects.order_by('-id')[0:3]  # выборка последних 3 продуктов
    print('Последние 3 добавленных в каталог продукта:')
    for product in last_products:
        print(product)
    products = Product.objects.all()
    context = {
        'object_list': products,
        'title': 'Интернет-магазин'
    }
    return render(request, 'home.html', context)


def product_details(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product,
        'title': product.title
    }
    return render(request, 'product_details.html', context)


def contacts(request):
    """Контроллер отображения страницы с контактными данными"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}; телефон: {phone}; сообщение: {message}')
    return render(request, 'contacts.html')
