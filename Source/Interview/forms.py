from django import forms
from django.forms import widgets

from Interview.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]
        widgets = {
            "question": widgets.Textarea(attrs={"cols": 20, "rows": 6})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["option"]
        widgets = {
            "option": widgets.Textarea(attrs={"cols": 20, "rows": 6}),
        }


