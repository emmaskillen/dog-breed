from django.urls import path
from application import views


urlpatterns = [
    path('', views.application, name='application'),
   # path('', views.get_dogs, name = "get_dogs"),

]
