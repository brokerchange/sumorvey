from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Question, Answer
from random import randrange
from .forms import RandomForm


def question_list(request):
    if request.user.is_staff:
        questions = Question.objects.order_by('created')
        answers = Answer.objects.order_by('pk')
        return render(request, 'survey/question_list.html', {'questions': questions, 'answers': answers})
    else:
        return redirect(question_random)


def question_random(request):
    # Present a random survey question to visitors
    # Get a list of possible questions based on the primary keys of all questions
    question_todo = [todo for todo in Question.objects.all().values_list('id', flat=True)]
    # Check the session for previously answered questions, rm them from todo
    if 'answered' in request.session:
        for answer in request.session['answered']:
            question_todo.remove(answer)
    # Select a random pk, check it for satisfying prereqs (if applicable), loop until pass
    question_good = 0
    while question_good < 1:
        if len(question_todo) > 1:
            question_num = question_todo.pop(randrange(len(question_todo)))
        elif len(question_todo) == 1:
            question_num = question_todo.pop()
        else:
            question_num = 0
            break
        # Check for prereq, test if that answer is in session previous answers
        question_prereq = Question.objects.get(pk=question_num).prereq
        if question_prereq:
            if 'responses' in request.session:
                if question_prereq.pk in request.session['responses']:
                    question_good = 1
        else:
            question_good = 1
    # If we're out of valid questions, pass apology instead of form
    if not question_num:
        question = ""
        form = "All out of questions, please try again later."
    else:
        question = get_object_or_404(Question, pk=question_num)
        form = RandomForm(question_num=question_num)
    if request.method == "POST":
        answer = get_object_or_404(Answer, pk=request.POST['vote'])
        question = get_object_or_404(Question, pk=answer.parent.pk)
        answer.vote()
        if 'responses' in request.session:
            request.session['responses'].append(answer.pk)
            request.session.modified = True
        else:
            request.session['responses'] = [answer.pk]
            request.session.modified = True
        if 'answered' in request.session:
            request.session['answered'].append(answer.parent.pk)
            request.session.modified = True
        else:
            request.session['answered'] = [answer.parent.pk]
            request.session.modified = True
        return redirect('question_random')
    return render(request, 'survey/question_random.html', {'question': question, 'form': form})


def question_detail(request, pk):
    if request.user.is_staff:
        question = get_object_or_404(Question, pk=pk)
        answers = get_list_or_404(Answer, parent=pk)
        return render(request, 'survey/question_detail.html', {'question': question, 'answers': answers})
    else:
        return redirect(question_random)


def purge_session(request):
    if request.user.is_staff:
        del request.session['answered']
        del request.session['responses']
        request.session.modified = True
    return redirect(question_random)


def purge_results(request):
    if request.user.is_staff:
        for answer in Answer.objects.all():
            answer.votes = 0
            answer.save()
        return redirect(question_list)
    else:
        return redirect(question_random)
