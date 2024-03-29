from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password']
        
class addQuestionForm(ModelForm):
    class Meta:
        model = QuestModel
        fields = "__all__"
        
