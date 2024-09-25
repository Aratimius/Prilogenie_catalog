from django.forms import inlineformset_factory
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Интернет-магазин'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = Product.objects.get(pk=self.kwargs['pk'])
        all_versions = Version.objects.all()
        product_versions = []
        for version in all_versions:
            if version.product == context_data['title']:
                product_versions.append(version)
        context_data['versions'] = product_versions
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    #  РЕАЛИЗАЦИЯ РАБОТЫ С ФОРМСЕТОМ:
    def get_context_data(self, **kwargs):
        """Добавления формсета в контекст"""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Сохранение данных дополнительно в формсет"""
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'Имя: {name}; телефон: {phone}; сообщение: {message}')
        return self.get(request, *args, **kwargs)
