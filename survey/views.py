from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from random import randint
from .forms import RandomForm


def question_list(request):
    questions = Question.objects.order_by('created')
    answers = Answer.objects.order_by('pk')
    return render(request, 'survey/question_list.html', {'questions': questions, 'answers': answers})


def question_random(request):
    question_num = randint(1, Question.objects.all().count())
    question = Question.objects.get(pk=question_num)
    answers = Answer.objects.filter(parent=question_num)
    form = RandomForm(question_num=question_num)
    return render(request, 'survey/question_random.html',
        {'question': question, 'question_num': question_num, 'answers': answers, 'form': form, })


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = get_object_or_404(Answer, parent=pk)
    return render(request, 'survey/question_detail.html', {'question': question, 'answers': answers})
