from django import forms
from .models import *

class FormComment(forms.Form):
    title = forms.CharField(max_length=50,label="тема",initial="тема")
    content = forms.CharField(label="контент",required=False,widget=forms.Textarea(
        attrs={"cols":80,"rows":10,"class":"form-input",'placeholder': 'Ваш коментарий'}
    ))
    published = forms.BooleanField(label="опубликовано")

class FormProvider(forms.ModelForm):
    class Meta():
        model = Provider
        fields = ["name_prov","adress"]
        widgets = {
            "name_prov": forms.TextInput(attrs={"placeholder":"производитель","class":"form-control"}),
            "adress" : forms.Textarea(attrs={"cols":50,"rows":5})
        }
