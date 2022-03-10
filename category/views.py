from dataclasses import fields

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from category.forms import CategoryForm
from category.models import Category


# Create your views here.
class CategoryListView(CreateView, ListView):
    model = Category
    # fields = ['name']
    paginate_by = 5
    form_class = CategoryForm
    queryset = Category.objects.all().order_by('name')
    template_name = 'category/category_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.get_form()
        return context

    # If form post redirect to ModelCreate View
    def post(self, request, *args, **kwargs):
        return CategoryCreateView.as_view()(request)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('category-list')

    