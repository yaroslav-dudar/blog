#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db.models import Sum
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Answer, Poll, PollResult, PossiblePollResult
from .serializers import (QuestionSerializer,
    PollResultSerializer, PossiblePollResultSerializer)

@api_view(['GET'])
def get_poll(request, pk):
    try:
        poll_questions = Poll.objects.get(id=pk).questions
    except Poll.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = QuestionSerializer(poll_questions, many=True)
    return Response(serializer.data)
        

@api_view(['POST'])
def save_poll_results(request):
    serializer = PollResultSerializer(data=request.DATA)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_possible_poll_result(request):
    poll_id = request.GET.get('poll_id')
    total_value = request.GET.get('total_value')
    try:
        possible_result = PossiblePollResult.objects.get(
            min__lte=total_value, max__gte=total_value, poll=poll_id)
    except PossiblePollResult.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PossiblePollResultSerializer(possible_result)
    return Response(serializer.data)