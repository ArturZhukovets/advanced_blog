from django import forms
from .models import Dictionary


class DictionaryForm(forms.ModelForm):
    """Форма создаётся от метода ModelForm - непосредственно связана с Моделью из бд"""
    class Meta:
        """В этом классе необходимо сообщить НА ОСНОВАНИИ КАКОЙ МОДЕЛИ будет создана ФОРМА (model=Dictionary)
        Вторым аргументом указываю поля которые необходимо отобразить (в виде списка) - ОБЯЗАТЕЛЬНОЕ ПОЛЕ!
        Значения Валидации для созданной формы, наследованной от модели будет ТАКИМ ЖЕ КАК И У МОДЕЛИ (max_length и т.д)
        Для того, чтобы написать текст ошибок используем атрибут error_massages"""
        model = Dictionary
        fields = '__all__'
        labels = {
            'word': "Слово на английском",
            'translate': "Слово на русском",
            'transcription': "Транскрипция (не обязательно)",
            'context': "Контекст (не обязательно)",
        }
        error_massages = {
            'word': {
                'max_length': 'У данного слова превышен лимит символов',
                'required': 'Введите хотя бы один символ',
            },
            'translate': {
                'max_length': 'У данного слова превышен лимит символов',
                'required': 'Введите хотя бы один символ',
            }
        }
        # localized_fields = False
