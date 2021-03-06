from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime
from django.core.validators import RegexValidator

# Create your models here.

class Quiz(models.Model):
	word = models.CharField(max_length=20)
	meaning   = models.CharField(max_length=100)
	phrase  = models.CharField(max_length=100)
	sentence  = models.CharField(max_length=200)
	image_url = models.ImageField(upload_to = 'img/')

	def __unicode__(self):
		return self.word


class User(models.Model):
	name_regx = RegexValidator(regex=r"^[a-zA-Z]{3,20}$", message="This is not a valid username")
	username = models.CharField(unique=True,max_length=20, validators = [name_regx])
	email = models.EmailField(unique = True)
	password = models.CharField(max_length=20)
	score = models.CharField(max_length = 1000,default = "")

	def __unicode__(self):
		return self.username