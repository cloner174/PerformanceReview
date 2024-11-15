#
from django import forms
from core.models import Answer, Question

class EvaluationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        questions = Question.objects.all()
        for question in questions:
            self.fields[f'question_{question.id}'] = forms.CharField(
                label=question.text,
                widget=forms.Textarea
            )
    
#cloner174