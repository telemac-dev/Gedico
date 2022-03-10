from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Nome da categoria', max_length=50, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=50)
    
    def __str__(self):
        return self.name
