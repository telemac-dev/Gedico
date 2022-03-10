from django import forms

from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label='Nome da categoria',
                           widget= forms.TextInput
                           (attrs={'class':'form-control',
				   'id':'id_catName'}))
    class Meta:
        model = Category 
        fields = ['name']

    # helper = FormHelper()
    # helper.form_class = 'form-group'
    # helper.layout = Layout(
    #     Field('name', css_class='form-control mb-3'),
    #     Field('slug', css_class='form-control'),
    # )

