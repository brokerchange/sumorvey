from django.db import models
from django.utils import timezone

class Question(models.Model):
    prereq = models.ForeignKey('Answer', blank=True, null=True)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)

    def answers(self):
        answer_count = 0
        for answer in Answer.objects.filter(question=self.pk):
            answer_count += answer.votes
        return answer_count

    def __str__(self):
        return self.text

class Answer(models.Model):
    parent = models.ForeignKey('Question')
    text = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)

    def vote(self):
        self.votes += 1
        self.save()

    def reset(self):
        self.votes = 0
        self.save()

    def __str__(self):
        return self.text