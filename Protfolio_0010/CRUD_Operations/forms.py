from django import forms
from django.forms import ModelForm,widgets
from CRUD_Operations.models import image_gallary,newsTable 

class insertForms(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your Emial"}))
    topic=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Write Topic name"}))
    describe=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"Freely write ..."}))

class gallaryForm(forms.ModelForm):
    class Meta:
        model=image_gallary
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }
        # fields=['name','image']

class newsForm(forms.ModelForm):
    class Meta:
        model=newsTable
        fields="__all__"
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'topic':forms.TextInput(attrs={'class':'form-control'}),
            'describe':forms.Textarea(attrs={'class':'form-control'}),
            'field':forms.FileInput(attrs={'class':'form-control'}),
        }
        # fields=['name','topic','describe','field']

# class gallery2(forms.ModelForm):
#     name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Name"}))
#     image=forms.ImageField()