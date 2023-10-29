from django.shortcuts import render
import requests
from application.models import Dog 


# function for displaying breed search results
def application(request):
    todos = []
    if 'name' in request.GET:
        name = request.GET['name']
        response = requests.get('https://api.algobook.info/v1/dogs/search/%s' % name)
        todos = response.json()
        for i in todos:
            dog_data = Dog(
                name = i['name'],
                age = i['lifespan'],
                weight = i['weightLbs'],
                height = i['heightInches'],
                traits = i['temperament'],
                image_url = i['imgUrl']
            )
            dog_data.save()
            todos = Dog.objects.all().order_by('-id')
    return render(request, 'application.html', {"todos":todos})


