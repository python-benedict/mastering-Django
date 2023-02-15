from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, world. You are at the pool index')

def detail(request, question_id):
    return HttpResponse("you are looking at question %s" %question_id)