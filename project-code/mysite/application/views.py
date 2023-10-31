from django.shortcuts import render
import requests
from application.models import Dog, Dog_2


# function for displaying breed search results table 1
def table_1(request):
    table1 = []
    
    # if searched name entered in search 1
    if 'name' in request.GET:
        name = request.GET['name']
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
            table1 = Dog.objects.filter(name=dog_data.name).order_by('-id')[:1]
    
    return render(request, 'application.html', {"table1":table1})
        #return render(request, 'application.html', {"todos":todos})

def table_2(request):
    table2 = []
    if 'name2' in request.GET:
        
        name_2 = request.GET['name2']
        response = requests.get('https://api.algobook.info/v1/dogs/search/%s' % name_2)
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
            table2 = Dog_2.objects.filter(name_2=dog_data_2.name_2).order_by('-id')[:1]

        #return render(request, 'application.html', {"todos_2":todos_2})
    return render(request, 'table-2.html', {"table2":table2})

"""

def application(request):
    todos_2 = []
    if 'name2' in request.GET:
        name = request.GET['name2']
        response = requests.get('https://api.algobook.info/v1/dogs/search/%s' % name)
        todos_2 = response.json()
        
        for i in todos_2:   
            dog_data_2 = Dog_2(
                name_2 = i['name'],
                age_2 = i['lifespan'],
                weight_2 = i['weightLbs'],
                height_2 = i['heightInches'],
                traits_2 = i['temperament'],
                image_url_2 = i['imgUrl']
                )
            dog_data_2.save()
            todos_2 = Dog_2.objects.filter(name=dog_data_2.name_2).order_by('-id')[:1]
    
    return render(request, 'table2.html', {"todos_2":todos_2})
"""