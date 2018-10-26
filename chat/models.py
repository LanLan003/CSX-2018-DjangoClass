from django.db import models
from django.conf import settings
from datetime import datetime


class Article(models.Model):
	name = models.CharField(max_length=10, blank=False)
	topic = models.CharField(max_length=20, blank=False)
	content = models.TextField(max_length=256, blank=False)
	#time = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.user_name + '-' + self.topic

		
class Message(models.Model):
	talker = models.CharField(max_length=10, blank=False)
	msg = models.TextField(max_length=64, blank=False)
	#time = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.talker + '-' + self.msg