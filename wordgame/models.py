from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.

class Quiz(models.Model):
	main_word = models.CharField(max_length=20)
	question  = models.CharField(max_length=100)
	sentence  = models.CharField(max_length=200)
	meaning   = models.CharField(max_length=100)
	image_url = models.CharField(max_length=100)

	def __unicode__(self):
		return self.main_word


class User(models.Model):
	user_name = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	score = models.IntegerField(default =0)

	def __unicode__(self):
		return self.user_name

