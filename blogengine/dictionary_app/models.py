from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Dictionary(models.Model):
    word = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    translate = models.CharField(max_length=20,)
    transcription = models.CharField(max_length=20, blank=True, default='')
    context = models.TextField(blank=True, default='')