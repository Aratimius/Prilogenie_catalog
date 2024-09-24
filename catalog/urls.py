from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ContactsTemplateView, ProductListView


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
]
