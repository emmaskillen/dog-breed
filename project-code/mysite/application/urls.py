from django.urls import path
from application import views


urlpatterns = [
    path('', views.table_1, name='table_1'),
    path('', views.table_2, name='table_2'),
    
   # path('', views.get_dogs, name = "get_dogs"),

]
