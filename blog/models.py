from django.db import models
from django.utils import timezone

class Post(models.Model): 								# models.model tells django that is is a django model, so it should be saved in the database
	
	#properites
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)	 		# text with a limited number of characters
	text = models.TextField()							# long text wtihout a limit, like a blog post
	created_date = models.DateTimeField(                # date and time
			default=timezone.now)
	published_date = models.DateTimeField(
					blank=True, null =True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

