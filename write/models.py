from django.db import models
import datetime

# Create your models here.
class Writing(models.Model):
	content = models.TextField()
	date_created = models.DateField(default=datetime.date.today())
	
	def __str__(self):
		return self.date_created.strftime('%b. %d, 20%y')