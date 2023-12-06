from django.urls import path
from application import views


urlpatterns = [
    path('', views.application, name='application'),
    #path('search/', views.search_view, name='search_view'),
    path('search/', views.search_view, name='search_view'),
    # path('', views.get_dogs, name = "get_dogs"), 
    path('fun_fact_button/', views.fun_fact_button, name='fun_fact_button')
    
]