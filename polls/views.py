from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.

# ListView -- display a list of objects
# The ListView generic view uses a default template called <app name>/<model name>_list.html
# For ListView, the automatically generated context variable is question_list. To override this use context_object_name attribute.
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		# Return the last five published questions
		#return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

# DetailView -- display a detail page for a particular type of object.
# The DetailView generic view expects the primary key captured from the URL to be called 'pk' .
# By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html .
# In our case, the default template name would "polls/question_detail.html"
# The 'template_name' attribute is used to tell Django to use a specific template name
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# The following only vote func is needed.

def index(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
	
	"""
	v1
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
	"""

	"""
	V2
	# The code loads the template called polls/index.html and passes it a context.
	# The context is a dict mapping template variable names to Python objects.
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))
	"""

	# v3	
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


def hgDemo(request):
	return HttpResponse("This is HappyGuy Django Demo app.")

def detail(request, question_id):
	#return HttpResponse("You're looking at question %s." % question_id)

	"""
	# v2
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	
	return render(request, 'polls/detail.html', {'question': question})
	"""

	# v3
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	#response = "You're looking at the results of question %s."
	#return HttpResponse(response % question_id)

	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

# same as before
def vote(request, question_id):
	#return HttpResponse("You're voting on question %s." % question_id)
	question = get_object_or_404(Question, pk=question_id)
	
	try:
		# request.POST is a dict-like object that lets you access submitted data by key name
		# Django also provides request.GET for accessing GET data in the same way
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		# You should always return an HttpResponseRedirect after successfully dealing with POST data
		return HttpResponseRedirect( reverse('polls:results', args=(question.id,)) )


