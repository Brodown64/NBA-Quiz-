from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import *

import random

# Create your views here.
def home(request):
	context = {'catgories': Types.objects.all()}

	if request.GET.get('gfg'):
		return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")

	return render (request, 'home.html', context)
	#creates categories, and calls gfg from (what i think the NBAQuiz folder, or just a general 'quiz' that you just write)

def quiz(request):
	context = {'gfg': request.GET.get('gfg')}
	return render(request, 'quiz.html', context)
	#references a quiz.html that we'll build later

def get_quiz(request):
	try:
		question_objs = Question.objects.all()
		# problem child maybe

		if request.GET.get('gfg'):
			question_objs = question_objs.filter(gfg__gfg_name__icontains = request.GET.get('gfg'))

		question_objs = list(question_objs)
		data = []
		random.shuffle(question_objs)

		for question_obj in question_objs:

			data.append({
				"uid" : question_obj.uid,
				"gfg": question_obj.gfg.gfg_name,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answer" : question_obj.get_answers(),
			})

			payload = {'status': True, 'data': data}

			return JsonResponse(payload)
			#calls questions with 5 different types of data inside, goes to a Json file
	except Exception as e:
		print(e)
		return HttpResponse("Something went wrong")
			
def todos(request):
	items = TodoItem.objects.all()
	return render(request, "todos.html", {"todos": items})
