from django.shortcuts import render,redirect
import requests,json
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
# Create your views here.
def index(request):

    mydict ={
        "result" : False
    }
    return render(request,'index.html',context=mydict)

def search(request):
    if request.method == "POST":
        try:
            city=request.POST['query']
            city=city.lower()
            API_KEY="3891916b2f364e56d63c5d9ee9a57228"
            urlPart1 = "http://api.openweathermap.org/data/2.5/weather?appid="+str(API_KEY)
            urlPart2 = "&q="+str(city)+"&units=metric"
            url = urlPart1+urlPart2
            result = requests.get(url).json()
            mydict = {
            "result" : True,
            "error" : False,
            "city" : city,
            "temp" : result["main"]["temp"],
            "mintemp" : result["main"]["temp_min"],
            "maxtemp"  : result["main"]["temp_max"],
            "humidity" : result["main"]["humidity"],
            "visibility" : result["visibility"],
            "windspeed" : result["wind"]["speed"]
            }
            print(mydict)
            return render(request,"index.html",context=mydict)
        except:                
            mydict = {
                "error" : True
            }
            return render(request,"index.html",context=mydict)
    