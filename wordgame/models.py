from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.

class word_gane_quiz(models.Model):
	main_word = models.charField(max_length=20)
	question = models.charField(max_length=100)
	sentence = models.charField(max_length=200)
	meaning = models.charField(max_length=100)
	image_url = models.charField(max_length=100)

