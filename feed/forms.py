from django import forms 

class PostForm(forms.Form):
    text = forms.CharField(label="Photo title")
    image = forms.FileField()
