from django.urls import path
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('<slug:slug>',post,name='post'),
    path('programacion/',Programacion.as_view(),name='programacion'),
    path('tecnologia/',Tecnologia.as_view(),name='tecnologia'),

]
