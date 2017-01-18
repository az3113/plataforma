from django.db import models
from usuario.models import usuario
# Create your models here.
''' 
nombre
'''
class Categoria(models.Model):
	ANIME ='ani'
	VIRTUALIZACION ='vir'
	PROGRAMACION = 'pro'
	CATEGORIES_CHOICES = (
	(ANIME,'anime'),
	(VIRTUALIZACION,'virtualizacion'),
	(PROGRAMACION,'programacion'))
	nombre = models.CharField(choices=CATEGORIES_CHOICES,default=ANIME, max_length=100)


class Curso(models.Model):
	categoria= models.ForeignKey(Categoria,null=True, blank=True)
	name = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	usuario = models.ForeignKey(usuario,null=True, blank=True)
	imagen = models.ImageField(upload_to='imagenes/')
	codigo = models.CharField(max_length=5)

class Tema(models.Model):
	titulo = models.CharField(max_length=100)
	codigo = models.CharField(max_length=5)
	descripcion = models.CharField(max_length=100)
	curso = models.ForeignKey(Curso,null=True, blank=True)
	
class Video(models.Model):
	tema = models.ForeignKey(Tema,null=True, blank=True)
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='document/')
	

 

class Document(models.Model):
	titulo = models.CharField(max_length=100)


class Comment(models.Model):
	user = models.CharField(max_length=250)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)
	tema =models.ForeignKey(Tema,null=True,blank=True)
	def approved(self):
		self.approved = True
		self.save()
	def __str__(self):
		return self.user
		
class Reply(models.Model):
	comment = models.ForeignKey(Comment,null=True,blank=True)
	user = models.CharField(max_length=250)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

'''
 
https://blog.enriqueoriol.com/2014/07/upload-de-imagenes-con-django.html
'''
'''class Comment(models.Model):
	post = models.ForeignKey(Document, null=True, blank=True)
	user = models.CharField(max_length=250)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	approved = models.BooleanField(default=False)

	def approved(self):
		self.approved = True
		self.save()
	def __str__(self):
		return self.user
'''
