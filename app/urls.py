from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post_student/', views.post_student),
    path('get_student/', views.get_student),
    
    

]

