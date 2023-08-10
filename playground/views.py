from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> view function -> response
# view function is a request handler
# not to be confused with templates

def say_hello(request):
  # pull data from the database
  # transform data
  # send emails
    return HttpResponse("Hello World")
    # return render(request, "hello.html")