from django.urls import path
from . import views
#from django.urls import path, include <- add this to line 17
# #if local host isnt open and is stuck on the django template and isn't showing hey welcome 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.donate, name='donate'),
] 
