
from django.urls import path

from category.views import CategoryCreateView, CategoryDeleteView, CategoryListView, CategoryUpdateView

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='category-list'),
    path('new/', CategoryCreateView.as_view(), name='category-new'),
    path('edit/<int:pk>', CategoryUpdateView.as_view(), name='category-edit'),
    path('delete/<int:pk>', CategoryDeleteView.as_view(), name='category-delete'),

]
