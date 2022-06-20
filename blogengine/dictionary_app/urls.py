from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DictionaryMainViews.as_view(), name='dictionary'),
    path('add_a_word', views.AddWordForm.as_view(), name='new-word'),
    path('<int:word_id>', views.UpdateForm.as_view(), name='update'),
]