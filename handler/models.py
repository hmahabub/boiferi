from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class author(models.Model):
	author_name= models.CharField(max_length=100)
	author_bio = models.TextField(blank=True)

	def __str__(self):
		return self.author_name

class book_list(models.Model):
	
	book_name		= models.CharField(max_length=100)
	Author_name = models.ForeignKey(
        author,
        on_delete=models.CASCADE
    )
	book_category 	= models.CharField(max_length=100)

	def __str__(self):
		return self.book_name

class history(models.Model):
	book_id= models.IntegerField()
	user_id = models.IntegerField()
	borrow_date = models.DateField()


class blog_post(models.Model):
	title = models.CharField(max_length=100)
	detail = models.TextField()
	user_id =models.IntegerField()
	user_name= models.CharField(max_length=100, blank=True)
	publish_date = models.DateField(default=timezone.now(),blank=True)
	class Meta:
		get_latest_by = "detail"

class profile_info(models.Model):
	user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=0,
    )
	gender= models.CharField(max_length= 10,blank=True, choices=[('male','male'),('female','female'),('others','others')])
	bio = models.TextField(blank=True)
	def __str__(self):
		return self.user.username