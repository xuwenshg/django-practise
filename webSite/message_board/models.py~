from django.db import models

# Create your models here.

class Users(models.Model):
	name = models.CharField(max_length=30)
	passwd = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
	class Meta:
		ordering=['name']

class Messages(models.Model):
	title = models.CharField(max_length=30)
	userid = models.ForeignKey(Users)
	content = models.CharField(max_length=200)
	date = models.DateField()

	def __unicode__(self):
		return self.name
	class Meta:
		ordering=['title']

