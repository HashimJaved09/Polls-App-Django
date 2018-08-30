from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from .models import Question

# Create your views here.

def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:6]
    context = {'latest_question':latest_question}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #q = Question.objects.get(pk = question_id)
    q = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'q':q})

def result(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'q':q})

def vote(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = q.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {'q':q, 'error_msg':"Please! Select an Option..."})
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result', args=(q.id,)))

def fun(request):
    return HttpResponse('fun function called!')