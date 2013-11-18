from django.db import models
from django.contrib.auth.models import User
import string
import random


class Userg(models.Model):
	user = models.OneToOneField(User);
	name = models.CharField(max_length=12)
	date_created = models.DateTimeField()
	current_points = models.IntegerField()
	cash = models.FloatField()
	point_multiplier = models.FloatField()
	def ___repr__(self):
		return self.name
	def ___str__(self):
		return self.name
	#def get_username(self):
	#	return self.auth_user.get_username()
	def related_user_email(self, obj):
		return obj.user.email
	def create_post(self,title,description,price):
		p = Post(name = title,description = description,price = price,user_created = self)
		p.save()
		self.current_points += self.determine_points(p)
		self.save()
	def comment_post(self,post,comment):
		c = Comment(parent_post = post, text = comment, user_created = self, date_created=now() )
		c.save()
		self.current_points += self.determine_points(c)
		self.save()
	def like_post(self,post):
		l = Like(parent_post = post, user_created = self, date_created = now() )
		l.save()		
	def determine_points(self,post):
		return self.point_multiplier*strlen(post.description)
		# TODO Finish this 

class Post(models.Model):
	name = models.CharField(max_length=12)
	url = models.CharField(max_length=200)
	photo = models.FileField(upload_to="files")
	description = models.TextField()
	price = models.FloatField(default=1.00)
	userg_created = models.ForeignKey(Userg, blank=True, null=True)
	user_created = models.CharField(max_length=12)	
	user_auth_created = models.ForeignKey(User, blank=True, null=True)
	def __repr__(self):
		return self.name+" by "+self.user_created.repr()
	def get_model_fields(model):
		return model._meta.fields
	def create_hash(self, size=8, chars=string.ascii_uppercase + string.digits):
		hash_string = ''.join(random.choice(chars) for x in range(size))
		ph = Post_Hash.objects.filter(hash=hash_string)
		if ph.count() == 0:
			return hash_string
		else:
			return create_hash(size,chars)
	def get_related_post_hash(self):
		ph = Post_Hash.objects.get(post = self)
		return ph.hash 
	
class Post_Hash(models.Model):
	post = models.ForeignKey(Post)
	hash = models.CharField(max_length=8, unique=True)		 

class Comment(models.Model):
	parent_post = models.ForeignKey(Post)
	text = models.TextField()
	user_created = models.ForeignKey(Userg)
	date_created = models.DateTimeField()
	def __repr__(self):
                return self.user_created.repr()+" on "+self.date_created

class Like(models.Model):
	parent_post = models.ForeignKey(Post)
	user_created = models.ForeignKey(Userg)
	date_created = models.DateTimeField()
	def __repr__(self):
                return self.user_created.repr()+" on "+self.date_created

class Lottery(models.Model):
	current_points = models.IntegerField()
	current_cash = models.FloatField()
	def __str__(self):
                return self.pool_total
	def draw(self,users):
		# TODO - Use the points sytem in random choosing
		u = random.choice(users)
		u.cash += self.current_cash
		self.current_cash = 0
		u.save()
		self.save()
		return "Congrats "+str(u)+"!"

