from django.db import models

class Question(models.Model):
    description = models.CharField(max_length=1024)
    multipe_choice = models.BooleanField(default=False)

    def __unicode__(self):
        return self.description


class Answer(models.Model):
    text = models.CharField(max_length=1024)
    question_answers = models.ForeignKey(Question, related_name='answers')
    value = models.FloatField()

    def __unicode__(self):
        return self.text

        
class Poll(models.Model):
    name = models.CharField(max_length=256)
    questions = models.ManyToManyField(Question)

    def __unicode__(self):
        return self.name


class PollResult(models.Model):
    poll = models.ForeignKey(Poll)
    date = models.DateTimeField(auto_now_add=True)
    total_value = models.FloatField()

    def __unicode__(self):
        return '%s(%s)' % (self.poll.name, self.date)


class PossiblePollResult(models.Model):
    poll = models.ForeignKey(Poll)
    min = models.FloatField()
    max = models.FloatField()
    image = models.CharField(max_length=256)
    text = models.CharField(max_length=2048)
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name
        