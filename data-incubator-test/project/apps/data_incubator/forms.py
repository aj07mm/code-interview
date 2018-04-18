from django import forms

class UploadImageForm(forms.Form):
    my_file = forms.ImageField()
