from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ContactsTemplateView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_details/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_details'),
    path('categories/', CategoryListView.as_view(), name='categories'),
]
