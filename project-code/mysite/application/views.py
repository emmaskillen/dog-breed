from django.shortcuts import render
import requests
from application.models import Dog, Dog_2
from .forms import searchForm, searchForm2
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# display main page
def application(request):
   return render(request, 'application.html')


# display search results (table 1 and table 2)
def search_view(request):
    breed1_name = request.GET.get('name', '')
    breed2_name = request.GET.get('name2', '')

    if breed1_name:
        table1 = grab_data_1(breed1_name)
    else:
        table1 = None

    if breed2_name:
        table2 = grab_data_2(breed2_name)
        #table2 = Dog.objects.filter(breed_name=breed2_name).first()
    else:
        table2 = None

    context = {
        'table1': table1,
        'table2': table2,
    }
    return render(request, 'application.html', context)


# get data from dog breed 1 from API
def grab_data_1(name):
    table1 = []
    #if 'name' in request.GET:
    #   name = request.GET['name']
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
        table2 = Dog_2.objects.filter(name_2=dog_data_2.name_2).order_by('-id')[:1]
    return table2

# press button for dog fact, call on microservice 
#@csrf_exempt
def fun_fact_button(request):
    #fact = "Fun Fact"
    #if request.method == "POST":
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    URL = "http://127.0.0.1:8004/fact"
    response = requests.get(URL)
    fact = response.json()["data"][0]["attributes"]["body"]
        #return JsonResponse({'fact':fact})
    return JsonResponse({'fact': fact})
    #return render(request, 'application.html', {'fact':fact})#, #{'fact':fact})

"""
def search_view(request):
    table1 = []
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
    print(table1)
    return render('application.html', {'table1':table1})   # return data object








# display search results (table 1 and table 2)
def search_view(request):
    if request.method == 'GET':
        form1 = searchForm(request.GET, prefix='form1')  # Prefix for the first form
        form2 = searchForm2(request.GET, prefix='form2')  # Prefix for the second form
        if form1.is_valid():
            search_term_1 = form1.cleaned_data.get('search_term')
            table1 = grab_data_1(search_term_1)
        else:
            table1 = Dog.objects.none()

        if form2.is_valid():
            search_term_2 = form2.cleaned_data.get('search_term')
            table2 = grab_data_2(search_term_2)
        else:
            table2 = Dog_2.objects.none()

    else:
        form1 = searchForm(prefix='form1')
        form2 = searchForm2(prefix='form2')
        table1 = Dog.objects.none()
        table2 = Dog_2.objects.none()
    
    return render(request, 'application.html', {'form1': form1, 'form2': form2, 'table1': table1, 'table2': table2})



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
    return render(request, 'application.html', {"table2":table2})

"""
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