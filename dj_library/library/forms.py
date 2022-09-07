from dataclasses import field, fields
import email
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Books, Members, Transactions
from . import forms

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email','password1', 'password2']

class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

class MembersForm(ModelForm):
    class Meta:
        model = Members
        fields = ['name', 'memberID']

class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = '__all__'