from django.db import models
from django.conf import settings


class Article(models.Model):
	user_name = models.CharField(max_length=10, blank=False)
	content = models.TextField(max_length=256, blank=False)

	def __str__(self):
		return self.user_name + '-' + self.content

		
class Message(models.Model):
	talker = models.CharField(max_length=10, blank=False)
	msg = models.TextField(max_length=64, blank=False)

	def __str__(self):
		return self.talker + '-' + self.msg