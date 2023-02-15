from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic

#함수형 뷰

# def index(request):
    
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
    
#     return render(request,'FirstApp\index.html',context)

# def detail(request, question_id):
#     # try:
#     question = get_object_or_404(Question,pk=question_id)
    
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     return render(request, 'FirstApp/detail.html',{'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'FirstApp/results.html', {'question':question})

def vote(requset, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=requset.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        return render(request, 'FirstApp/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

# 제너릭 뷰

class IndexView(generic.ListView):
    template_name = 'FirstApp\index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'FirstApp\detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'FirstApp/results.html'
    

    