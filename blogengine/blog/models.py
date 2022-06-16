from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def slug_generate(to_slug):
    """Генерируем новый slug при помощи slugify. Для создания уникального slug используем добавлять unix-time
    (время в секундах)"""
    new_slug = slugify(to_slug, allow_unicode=True)
    return f'{new_slug}-{str(int(time()))[-2:]}'


class Post(models.Model):
    """Необходимо переопределить метод .save() для создания поста, чтобы автоматически генерировать новый slug"""
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')  # related name default = post_set

    def get_absolute_url(self):
        """ reverse is generate link"""
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Переопределяем метод save для генерации слага при сохранении нового объекта.
         Если у экземпляра модели ещё не заполнен self.slug, то его новый слаг будет результатом работы функции slug_generation
         После того как slug будет сгенерирован, вызываем метод .save() у супер класса."""
        if not self.slug:
            self.slug = slug_generate(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        """Определение внутренних отношений модели. В данном случае критерий отношений - это сортировка"""
        ordering = ['-date_pub']


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slug_generate(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title']