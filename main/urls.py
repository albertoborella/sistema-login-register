from django.urls import path
from .views import home,libros,register,salir

urlpatterns = [
    path('', home, name='home'),
    path('libros/', libros, name='libros'),
    path('register/', register, name='register'),
    path('logout/', salir, name='logout'),
    
]
