# file: appName/views.py

from django.shortcuts import render, HttpResponse #import HttpResponse
from .models import*


from django.shortcuts import render, HttpResponse #import HttpResponse

# Create your views here.


from django.shortcuts import render, HttpResponse #import render

# Create your views here.


def home(request):
   return render(request, 'home.html')


def home(request):
   movie = movies.objects.all()
   
   data ={
      
      'movie':movie
   }
   
   
   return render(request, 'movie/home.html',data)

def detail(request, id):
   movie = movies.objects.get(id=id)
   
   data ={
      
      'movie':movie
   }
   
   
   return render(request, 'movie/detail.html',data)
def about(request):
   new = about.objects.all()
   news= {
      'new' : new
   }
   return render(request, 'movie/about.html',news)

# def contact_us(request):
#    return render(request, 'movie/contact.html')

def conacts_us(request):
   
   if request.method =='POST':
      user_name  = request.POST.get('name')
      user_email  = request.POST.get('email')
      user_text  = request.POST.get('text')
   
      obj = ContactInfo()
      
      obj.name = user_name
      obj.email =user_email
      obj.text = user_text
      obj.save()
   return render(request, 'contact.html')






