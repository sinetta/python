from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    context={}
    
    api_key='360e4bc3865e745ec844bd7ec054ca11'
    city='kochi'

    if request.method=='POST':
        if 'search' in request.POST:
            city=request.POST.get('search')
        
    # if not request.method:
        
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response=requests.get(url)
    data=response.json()
  

    weather=data['weather'][0]['description']
    temp=data['main']['temp']
    temp_max=data['main']['temp_max']
    temp_min=data['main']['temp_min']
    feels_like=data['main']['feels_like']



    context['weather']=weather
    context['temp']=temp
    context['temp_max']=temp_max
    context['temp_min']=temp_min
    context['feels_like']=feels_like
    context['city']=city 
      

    return render(request,'index.html',context)