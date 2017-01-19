from django import forms
from .models import Question, Answer


class RandomForm(forms.Form):
    ''' Boy, this is an ugly one. had to override init in order to read question_num to
    construct the list of possible answers'''

    def __init__(self, *args, **kwargs):
        self.question_num = kwargs.pop('question_num')
        super(RandomForm, self).__init__(*args, **kwargs)
        a_list = []
        for answer in Answer.objects.filter(parent=self.question_num):
            a_list.append((answer.pk, answer.text))
        self.fields['vote'] = forms.ChoiceField(widget=forms.RadioSelect, choices=a_list)
