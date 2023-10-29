from django.urls import path
from application import views


urlpatterns = [
    path('', views.application, name='application'),
    #path('', views.table2, name='table2'),
   # path('', views.get_dogs, name = "get_dogs"),

]
