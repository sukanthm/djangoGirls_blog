from .choices import * 
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)#, 'relevance',)
        #relevance = forms.ChoiceField(choices = RELEVANCE_CHOICES, required=True)