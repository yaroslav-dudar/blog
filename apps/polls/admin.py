from django.contrib import admin
from django import forms

from .models import Question, Answer, Poll, PollResult, PossiblePollResult

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('description', 'multipe_choice')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 100, 'rows': 4})
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'value', 'question_answers')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 100, 'rows': 4})
        }

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    form = AnswerForm

class PollResultAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionForm
    inlines = [ AnswerInline, ]

class AnswerAdmin(admin.ModelAdmin):
    form = AnswerForm

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll)
admin.site.register(PollResult, PollResultAdmin)
admin.site.register(PossiblePollResult)
