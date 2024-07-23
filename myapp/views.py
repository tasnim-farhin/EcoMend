from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from myapp.models import Category


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'
