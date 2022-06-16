from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin  # Для того чтобы неавторизованный пользователь не видел вьюхи с редактированием постов
# Ставиться в первичное наследование


def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        return search_list(request)
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)  # Если ключ 'page' не найден, то по умолчанию вернет 1
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    context = {
        'page_obj': page,
        'next_url': next_url,
        'prev_url': prev_url,
        'is_paginated': is_paginated,
    }

    return render(request, 'blog/index.html', context)


def search_list(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.filter(title__icontains=search_query)
    is_find = posts.count()

    return render(request, 'blog/searching_list.html', context={"page_obj": posts, "is_find": is_find})


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





