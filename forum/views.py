from django.shortcuts import render
from .models import Question, Answer
from .froms import AnswerForm


def question_list(request):
    data = Question.objects.all()
    return render(request, 'forum\list.html', {'data':data})


def question_detail(request, id):
    question = Question.objects.get(id=id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.question = question
            myform.save()

            #form = AnswerForm()
    else:
        form = AnswerForm()
    

    return render(request, 'forum\detail.html', {'question':question, 'form':form})



