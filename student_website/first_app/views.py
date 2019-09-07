from django.shortcuts import render
# added by Samyak Gaur 
from django.http import HttpResponse
from first_app.models import Entrie,Topic

# Create your views here.
# We will handle request and responses here

"""
created a fucntion index that takes a http request as an input 
and gives back a http response back 
Note: Each view must return a http response object 
***
as per our case our function returns a response regardless of the 
input 
***
We can also pass a html here.
"""
def index(request):
    helpdict = {'help_insert':' HELP PAGE'}
    return render(request,'first_app/home.html',context=helpdict)

# Now after creating this view we will map it to urls.py file

# This is for the templates dir mapping 

def help(request):
    helpdict = {'help_insert':' HELP PAGE'}
    return render(request,'first_app/help.html',context=helpdict)
"""
This function is called when we write 127.0.0.8000/help from 
projects url.py file 
which infact calls the first_app/help.html folder in templates folder and
injects the data dict into it
"""

#Now creating a index1 function for index.html file 
"""
This function links our index.html page and inserts the text into it
This is called by urls.py file of our first_app which is actually 
called by include function in the urls.py file in the main project
"""
def index1(request):
    entries_display = Entrie.objects.order_by('topics')
    index1dict = {'entries_display':entries_display}
    return render(request,'first_app/index.html',context=index1dict)

def report(request):
    entries_display = Entrie.objects.filter(year=2)
    index1dict = {'entries_display':entries_display}
    return render(request,'first_app/index12.html',context=index1dict)