from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):

   class Meta:
       model = Post
       fields = [
           'postCategory',
           'dateCreation',
           'title',
           'text',
           #'image',
       ]

   def clean(self):
       cleaned_data = super().clean()
       text = cleaned_data.get("text")
       if text is not None and len(text) < 20:
           raise ValidationError({
               "text": "Новость  не может быть менее 20 символов."
           })

       title = cleaned_data.get("title")
       if title == text:
           raise ValidationError(
               "Новость не должна быть идентична Заголовку."
           )

       return cleaned_data



