from django.db import models
import datetime

# Create your models here.
class Poll(models.Model): #model
	question = models.CharField(max_length=200) #fields
	pub_date = models.DateTimeField('date published')

#helpful representation of polls in the database
	def __unicode__(self):
		return self.question

	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	was_published_today.short_description = 'Published Today?' # new column heading

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()

	def __unicode__(self):
		return self.choice