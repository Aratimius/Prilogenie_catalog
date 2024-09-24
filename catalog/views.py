from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Интернет-магазин'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        object = Product.objects.get(pk=self.kwargs['pk'])
        context_data['title'] = object.title
        return context_data





class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'Имя: {name}; телефон: {phone}; сообщение: {message}')
        return self.get(request, *args, **kwargs)
