from django.db import models
from ckeditor.fields import RichTextField
class Categoria(models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField('Categoria',max_length=200,blank=False,null=False)
    estado=models.BooleanField('Categoria activada/Categoria no activada',default=True)
    fecha_creacion=models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id= models.AutoField(primary_key=True)
    nombres=models.CharField('Nombres De Autor',max_length=200,blank=False,null=False)
    apellidos=models.CharField('Apellidos De Autor',max_length=200,blank=False,null=False)
    facebook=models.URLField('Facebook',blank=True,null=True)
    twitter=models.URLField('Twitter',blank=True,null=True)
    instagram=models.URLField('Instagram',blank=True,null=True)
    web=models.URLField('Web',blank=True,null=True)
    email=models.URLField('Correo Electronico',blank=False,null=False)
    estado=models.BooleanField('Autor activo/Autor no activo',default=True)
    fecha_creacion=models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name= 'Autor'
        verbose_name_plural= 'Autores'

    def __str__(self):
        return "{},{}".format(self.apellidos,self.nombres)

class Post(models.Model):
    id= models.AutoField(primary_key=True)
    titulo=models.CharField('Titulo',max_length=90,blank=False,null=False)
    slug=models.CharField('Slug',max_length=100,blank=False,null=False)
    descripcion=models.CharField('Descripcion',max_length=110,blank=False,null=False)
    contenido=RichTextField()
    imagen=models.URLField(max_length=255,blank=False,null=False)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado=models.BooleanField('Publicado/No Publicado',default=True)
    fecha_creacion=models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name= 'Post'
        verbose_name_plural= 'Posts'

    def __str__(self):
        return self.titulo
