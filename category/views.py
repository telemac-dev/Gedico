from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from category.forms import CategoryForm
from category.models import Category


# Create your views here.
class CategoryListView(CreateView, ListView):
    model = Category
    paginate_by = 3
    form_class = CategoryForm
    template_name = 'category/category_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_name = self.request.GET.get('name') or None
        
        if filter_name:
            queryset = queryset.filter(name__contains=filter_name)
        else:
            queryset = Category.objects.all().order_by('name')
        return queryset
    

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


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = ".html"


class CategoryUpdateView(UpdateView, ListView):
    model = Category
    paginate_by = 3
    form_class = CategoryForm
    queryset = Category.objects.all().order_by('name')
    template_name = 'category/category_list.html'
    success_url = reverse_lazy('category-list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = self.get_form()
        return context

    # If form post redirect to ModelCreate View
    #def post(self, request, *args, **kwargs):
    #    return CategoryUpdateView.as_view()(request)

