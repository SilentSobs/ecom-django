from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes,name="routes"),
    path('products',views.getProduct,name='products'),
    path('product/<str:pk>', views.getProductById, name='product'),
]
