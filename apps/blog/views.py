from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,CreateView,View 
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


class Index(View):
    template_name='index.html'
    def queryset(self):
        queryset=Post.objects.filter(estado=True)
        return queryset



    def context(self):
        context={}
        context["post"]=self.queryset()
        return context


    def get(self,request,*args,**kwargs):
        return render(self.request,self.template_name,self.context())


class Programacion(ListView):
    model=Post
    template_name='programacion.html'
    queryset=Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Programacion')
    )
    context_object_name='post'

class Tecnologia(ListView):
    model=Post
    template_name='tecnologia.html'
    queryset=Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre='Tecnologia')
    )
    context_object_name='post'

def post(request,slug):
    queryset=Post.objects.get(slug=slug)
    return render(request,'post.html',{'post':queryset})

