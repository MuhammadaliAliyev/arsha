from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name

class Portfolio(models.Model):
	name = models.CharField(max_length = 30)
	owner = models.CharField(max_length = 30)
	deadline = models.DateField()
	link = models.CharField(max_length = 200)
	rasm1 = models.ImageField(upload_to='media')
	rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
	rasm3 = models.ImageField(upload_to='media',null=True,blank=True)
	type = models.ForeignKey(Category,on_delete=models.CASCADE)
	desc = models.TextField(null=True,blank=True)
	date = models.DateTimeField(auto_now=True)

class Clients(models.Model):
	rasm = models.ImageField(upload_to='media',null=True,blank=True)

class Services(models.Model):
	title = models.CharField(max_length = 30)
	text = models.TextField()

class Team(models.Model):
	ism = models.CharField(max_length=30)
	lavozim = models.CharField(max_length=50)
	desc = models.TextField()
	rasm = models.ImageField(upload_to='media')

class Add(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	subject = models.CharField(max_length=30)
	message = models.TextField()