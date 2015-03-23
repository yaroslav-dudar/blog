#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db.models import Sum

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Answer, Poll, PollResult
from .serializers import QuestionSerializer
from .utils import calculate_answers

@api_view(['GET'])
def get_poll(request, pk):
	poll_questions = Poll.objects.get(id=pk).questions
	serializer = QuestionSerializer(poll_questions, many=True)
	return Response(serializer.data)
		

@api_view(['POST'])
def save_poll_results(request):
	total_value = Answer.objects.filter(
		id__in=request.DATA['answers']).aggregate(Sum('value'))['value__sum']
	
	poll = Poll.objects.get(id=request.DATA['poll'])
	poll_result = PollResult(poll=poll, total_value=total_value)
	poll_result.save()

	return Response(calculate_answers(total_value), status=status.HTTP_201_CREATED)