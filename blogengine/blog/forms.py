from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def clean_slug(self):
        """В данном методе исключаем повторные значения поля slug, а также совпадение с именем create (т.к существует url по этому адресу)"""
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():   # if gt than 0 - True -> ValidationError
            raise ValidationError(f'Slug must be unique. We have "{new_slug}" already')

        return new_slug
    # def save(self):
    #     """Save method override. Returning saved values from the dictionary cleaned_data"""
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            # 'date_pub': forms.DateTimeInput(attrs={'class': 'form-control'}),  # non-editable
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()  # low register
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be unique. We have "{new_slug}" already')
        return new_slug