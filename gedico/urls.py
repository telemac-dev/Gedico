from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path


def my_view(request):
    return render(request, 'global/base.html')
    #return HttpResponse('<h1>Paz no Mundo !!!</h1>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('category.urls')),
    path('', my_view, name='paz'),
]

