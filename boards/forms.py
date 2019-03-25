from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=4000,widget=forms.Textarea(attrs={'rows':5,'placeholder':"What's in your mind"},
    ),help_text = "Max 4000 char long allowed")
    class Meta:
        fields = ['name','message']
        model = Topic