from django.shortcuts import render, redirect
from django.views import View
from .models import Dictionary
from .forms import DictionaryForm
from django.http.response import HttpResponse, HttpResponseRedirect


# Create your views here.


class DictionaryMainViews(View):

    def get(self, request):
        words = Dictionary.objects.all()
        context = {
            'words': words,
        }
        return render(request, 'dictionary_app/index.html', context)


class AddWordForm(View):
    def get(self, request):
        form = DictionaryForm()
        return render(request, 'dictionary_app/add_new_word.html', context={'form': form})

    def post(self, request):
        """ В методе POST request.POST - наполняет форму введёнными данными.
        Введенные данные отправляем в бд"""
        form = DictionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dictionary')
        else:
            error = 'The form is not valid, try again'
            return render(request, 'dictionary_app/add_new_word.html', context={'form': form, 'error': error})


class UpdateForm(View):
    """Обновление формы. Если запрос get - Отображает форму с данными взятого элемента из БД по id
    Если запрос POST - проверяет на валидность формы и если всё ок - отправляет обновления в БД."""

    def get(self, request, word_id):
        form_data = Dictionary.objects.get(id=word_id)
        form = DictionaryForm(instance=form_data)
        return render(request, 'dictionary_app/edit_word.html', context={'form': form,
                                                                         'model_obj': form_data})

    def post(self, request, word_id):
        form_data = Dictionary.objects.get(id=word_id)
        form = DictionaryForm(request.POST, instance=form_data)
        if form.is_valid():
            form.save()
            return redirect('dictionary')
        else:
            error = 'The form is not valid. Try again.'
            return render(request, 'dictionary_app/edit_word.html', context={'form': form,
                                                                             'error': error,
                                                                             'model_obj': form_data})
