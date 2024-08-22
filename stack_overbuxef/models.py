from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage 
from ckeditor_uploader.fields import RichTextUploadingField


#En las variables fsPhotos y fsMedia tiene las direcciones de los archivos donde se guardaran las fotos y otro tipo de
#contenido multimedia respectivamente.   Estas variables seran ocupadas en las clases Usuario, Consultas y Respuestas.
fsPhotos = FileSystemStorage(location="fotos_usuarios/")
fsMedia = FileSystemStorage(location="/media/Multimedia")

options = [[0, "No anónimo"], [1, "Anónimo"]]


#Esta clase se usara para crear la tabla categorias que va a tener los mensajes del foro.
#Cuenta con la variable nombre como atributo.
class Tag(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


#Esta clase se usara para crear la tabla Rol que tendra los roles de los usuarios creados.
#Cuenta con rol como atributo.
class Rol(models.Model):
    rol = models.CharField(max_length=20)
    def __str__(self):
        return self.rol  


# Esta clase se usara para crear la tabla Usuario que tendra os usuarios del sistema.
# Tiene como atributos foto en el que se tendra la foto asociada al usuario, rol el cual sera una llave foranea proveniente de
# la tabla Rol y los atributos correspondientes a la clase abstracta AbstractUser dada por Django.
class Usuario(AbstractUser):
    options = [
        ("ES", "Estudiante"),
        ("AD", "Administrador"),
        ("PR", "Profesor"),
    ]
    tipo = models.CharField(choices=options, max_length=2)
    foto = models.ImageField(upload_to=fsPhotos, blank=False, null=False, default="fotos_usuarios/default.png")


#Esta clase se usara para crear la tabla consulta que tendra todas las consultas que haga un usuario en el foro.
class Consulta(models.Model):
    titulo=models.CharField(blank=False, null=False,max_length=100)
    fecha_creacion=models.DateTimeField(default=timezone.now)
    mensaje = RichTextUploadingField('mensaje')
    creador=models.ForeignKey(Usuario, blank=False, null=False,on_delete=models.CASCADE)
    anonimo=models.BooleanField(null=False,default=0)
    multimedia = models.FileField(storage=fsMedia, blank=True, null=True)
    votar=models.IntegerField(default=0)
    users_liked = models.ManyToManyField(Usuario, related_name='consultas_liked', blank=True)
    users_disliked = models.ManyToManyField(Usuario, related_name='consultas_disliked', blank=True)


#Esta clase se usara para crear la tabla Respuesta que tendra todas las respuestas asociadas a alguna consulta.
class Respuesta(models.Model):
    mensaje = RichTextUploadingField('respuesta')
    creador=models.ForeignKey(Usuario,blank=False,null=False,on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(default=timezone.now)
    consulta=models.ForeignKey(Consulta,null=False,blank=False,on_delete=models.CASCADE)
    multimedia=models.FileField(storage=fsMedia,blank=True, null=True)
    votar=models.IntegerField(default=0)
    anonimo=models.BooleanField(null=False, default=0)
    users_liked = models.ManyToManyField(Usuario, related_name='respuestas_liked', blank=True)
    users_disliked = models.ManyToManyField(Usuario, related_name='respuestas_disliked', blank=True)


#Esta clase se usara para crear la tabla Consulta_respuesta que crea la relación entre las tablas Consulta y Respuesta
class Consulta_respuesta(models.Model):
    consulta=models.ForeignKey(Consulta,blank=False,null=False,on_delete=models.CASCADE)
    respuesta=models.ForeignKey(Respuesta,blank=True,null=True,on_delete=models.CASCADE)


#Esta clase se usara para crear la tabla Consulta-respuesta que crea la relación entre las tablas Consulta y Tag.
class Consulta_tag(models.Model):
    consulta=models.ForeignKey(Consulta,blank=False,null=False,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
