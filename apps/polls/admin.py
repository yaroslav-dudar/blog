from django.contrib import admin
from .models import Question, Answer, Poll, PollResult

class PollResultAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Poll)
admin.site.register(PollResult, PollResultAdmin)
