from django.contrib import admin
from .models import Question, Answer, Poll, PollResult

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(PollResult)
