from django import forms

from .models import Topic, Entry
from .widgets import ColorPickerWidget

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['text', ]
        labels = {'text': 'Topic name'}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', ]
        labels = {'text': 'Entry text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class SimpleForm(forms.Form):

    color = forms.CharField(label='Your favorite color', widget=ColorPickerWidget)
    username = forms.CharField(max_length=100, label='Your username')
    email = forms.CharField(label='Your email', widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_2']:
            self._errors["password"] = ["Password do not match"]  # Will raise a error message
            del form_data['password']

        return form_data