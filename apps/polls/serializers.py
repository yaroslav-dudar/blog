from rest_framework import serializers
from .models import Question, Answer, PollResult, PossiblePollResult

class AnswerSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Answer
        fields = ('text', 'id', 'value')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('description', 'answers')


class PollResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollResult


class PossiblePollResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = PossiblePollResult
        fields = ('image', 'text', 'name')
