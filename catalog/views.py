from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Version, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.services import get_objects_from_cache
from users.models import User


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Интернет-магазин'
    }

    def get_queryset(self):
        return get_objects_from_cache(Product)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = Product.objects.get(pk=self.kwargs['pk'])

        #  Достать все версии принадлежащие данному продукту:
        all_versions = Version.objects.all()
        product_versions = []
        for version in all_versions:
            if version.product == context_data['title']:
                product_versions.append(version)
        context_data['versions'] = product_versions
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        """Автоматическая привязка пользователя к созданному продукту"""
        product = form.save()
        user = self.request.user
        product.user = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user or user.is_superuser is True:
            return ProductForm
        elif (user.has_perm('catalog.can_edit_category') and user.has_perm('catalog.can_edit_description')
              and user.has_perm('catalog.set_published_status')):
            return ProductModeratorForm
        raise PermissionDenied

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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
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


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории продуктов'
    }

    def get_queryset(self):
        return get_objects_from_cache(Category)
