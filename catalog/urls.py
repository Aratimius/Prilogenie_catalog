from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ContactsTemplateView, ProductListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
]
