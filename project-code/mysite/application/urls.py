from django.urls import path
from application import views


urlpatterns = [
    path('', views.application, name='application'),
    path('search_view/', views.search_view, name='search_view'),
    path('fun_fact_button/', views.fun_fact_button, name='fun_fact_button')
    
]