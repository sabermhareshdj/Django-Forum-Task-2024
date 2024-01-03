from django.shortcuts import render
from .models import Question, Answer


def question_list(request):
    data = Question.objects.all()
    return render(request, 'forum\list.html', {'data':data})


def question_detail(request, id):
    question = Question.objects.get(id=id)
    

    return render(request, 'forum\detail.html', {'question':question})



