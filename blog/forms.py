from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'rows':15, 'cols':120}))

    class Meta:
        model = Blog
        fields = ["content"]




