
import datetime

from django.db import models
from django.utils import timezone

#from django.utils.encoing import python_2_unicode_compatile

# Create your models here.

# Each model is a subclass of django.db.models.Model
# Each model has a number of class vars, each of which represents a database field in the model
# Each field is an instance of Field class -- e.g., CharField for character field and DateTimeField for datetimes

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

