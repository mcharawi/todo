from django import forms
import re
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from todolist.models import *

class SignupForm(ModelForm):
	
	class Meta:
		model=User
		fields = "__all__"