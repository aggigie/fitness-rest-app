from django.urls import path
from fitness_pal import views


urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:pk>/', views.product_detail)
]
