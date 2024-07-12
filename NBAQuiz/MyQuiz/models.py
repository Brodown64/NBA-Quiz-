from django.db import models
import uuid
import random

# Create your models here.

class TodoItem(models.Model):
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

class BaseModel(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = True)
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)

	class Meta:
		abstract = True
# i think the creation date and updating of this quiz (answer: Timestamps)


# PROBLEM CHILD
class Types(BaseModel):
	gfg_name = models.CharField(max_length=100)
	def __str__(self) -> str:
		return self.gfg_name
# gfg probably accesses or is the key that builds the questions and answers, the self parameter accesses it.

class Question(BaseModel):
	gfg = models.ForeignKey(Types, related_name='gfg',on_delete= models.CASCADE)
	question = models.CharField(max_length=100)
	marks = models.IntegerField(default = 5)
	# foreign key calls back to the Types class, and the question field is built

	def __str__(self) -> str:
		return self.question
		# defines a self into a string (question)

	def get_answers(self):
		answer_objs = list(Answer.objects.filter(question = self))
		data = []
		random.shuffle(answer_objs)

		for answer_obj in answer_objs:
			data.append({
				'answer' : answer_obj.answer,
				'is_correct' : answer_obj.is_correct
				})
			return data
       #answers are being collected, and data is shuffled between answer and is correct for some reason


class Answer(BaseModel):
	question = models.ForeignKey(Question,related_name = 'question_answer', on_delete = models.CASCADE)
	answer = models.CharField(max_length=500)
	is_correct = models.BooleanField(default = False)

	def __str__(self) -> str:
		return self.answer
		# i guess receives an answer from data, and returns it

