from django import forms
from .models import Question, Answer
from sys import stderr


class RandomForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.question_num = kwargs.pop('question_num')
        super(RandomForm, self).__init__(*args, **kwargs)
        print(self.question_num, file=stderr)
        self.answers = Answer.objects.filter(parent=self.question_num)
        a_list = []
        for answer in self.answers:
            a_list.extend([answer.pk, answer.text])
        
        vote_choices = ((a_list[i], a_list[i + 1]) for i in range(0, len(a_list), 2))
        self.fields['vote'] = forms.ChoiceField(widget=forms.RadioSelect, choices=vote_choices)
