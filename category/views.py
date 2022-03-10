from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from category.forms import CategoryForm
from category.models import Category


# Create your views here.
class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all().order_by('name')
    template_name = 'category/category_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['form'] = CategoryForm()
        return context


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('category-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().order_by('name')
        return context
        