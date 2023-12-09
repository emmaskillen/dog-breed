from django.shortcuts import render
import requests
from application.models import Dog, Dog_2
from .forms import searchForm, searchForm2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json 

# display main page
def application(request):
   return render(request, 'application.html')


# display search results (table 1 and table 2)
def search_view(request):
    data = json.loads(request.body)
    breed1_name = data['dog_1']
    breed2_name = data['dog_2']
    
    if breed1_name:
        table1 = grab_data_1(breed1_name)
    else:
        table1 = "None"

    if breed2_name:
        table2 = grab_data_2(breed2_name)
        
    else:
        table2 = "None"

    context = {
        'table1': list(table1),
        'table2': list(table2),
    }
    
    return JsonResponse({'context':context})



# get data from dog breed 1 from API
def grab_data_1(name):
    table1 = []
    response = requests.get('https://api.algobook.info/v1/dogs/search/%s' % name)
    table1 = response.json()

    for i in table1:   
            dog_data = Dog(
                    name = i['name'],
                    age = i['lifespan'],
                    weight = i['weightLbs'],
                    height = i['heightInches'],
                    traits = i['temperament'],
                    image_url = i['imgUrl']
                    )
    dog_data.save()
    table1 = Dog.objects.filter(name=dog_data.name).order_by('-id')[:1].values()
    
    return table1   # return data object

# get data from API for dog breed 2
def grab_data_2(name2):
    table2 = []
    #name2 = request.GET['name2']
    response = requests.get('https://api.algobook.info/v1/dogs/search/%s' % name2)
    table2 = response.json()
    
    for i in table2:   
        dog_data_2 = Dog_2(
            name_2 = i['name'],
            age_2 = i['lifespan'],
            weight_2 = i['weightLbs'],
            height_2 = i['heightInches'],
            traits_2 = i['temperament'],
            image_url_2 = i['imgUrl']
            )
        dog_data_2.save()
        table2 = Dog_2.objects.filter(name_2=dog_data_2.name_2).order_by('-id')[:1].values()
    return table2

# press button for dog fact, call on microservice 
def fun_fact_button(request):
    URL = "http://127.0.0.1:8004/fact"
    response = requests.get(URL)
    fact = response.json()["data"][0]["attributes"]["body"]
        
    return JsonResponse({'fact': fact})
    







