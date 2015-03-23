from rest_framework import serializers
from .models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
		
	class Meta:
		model = Answer
		fields = ('text', 'id')


class QuestionSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True)

	class Meta:
		model = Question
		fields = ('description', 'answers')