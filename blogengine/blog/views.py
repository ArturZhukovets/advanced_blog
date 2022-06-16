from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin  # Для того чтобы неавторизованный пользователь не видел вьюхи с редактированием постов
# Ставиться в первичное наследование


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """LoginRequiredMixin имеет несколько атрибутов. Можно перенаправлять на url для регистрации пользователя,
    можно написать сообщение об отказе в разрешении"""
    form_model = PostForm
    template = 'blog/post_create.html'
    # login_url = '/admin'
    raise_exception = True   # output a 404 error message



class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html.'


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'





