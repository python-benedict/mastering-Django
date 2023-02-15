from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
def index(request):
    questions = Question.objects.all()
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(questions)

def detail(request, question_id):
    return HttpResponse("you are looking at question %s" %question_id)

def results(request, question_id):
    response = "you are looking at the response of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('you are voting on the question %s' %question_id)