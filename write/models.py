from django.db import models

# Create your models here.
class Writing(models.Model):
	content = models.TextField()
	date_created = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return self.date_created.strftime('%b. %d, 20%y')