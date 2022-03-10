
from django.urls import path

from category.views import CategoryCreateView, CategoryListView

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='category-list'),
    path('new/', CategoryCreateView.as_view(), name='category-new'),

]
