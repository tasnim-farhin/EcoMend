from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
]