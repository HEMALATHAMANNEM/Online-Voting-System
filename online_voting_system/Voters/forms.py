from django.forms import ModelForm
from django import forms
from .models import Voter,Candidate,Position,Votes

class VoterForm(ModelForm):
    class Meta:
        model=Voter
        fields='__all__'

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'},render_value=True),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
        }

class CandidateForm(ModelForm):
    class Meta:
        model=Candidate
        fields='__all__'

        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'bio':forms.TextInput(attrs={'class':'form-control'}),
        }

class PositionForm(ModelForm):
    class Meta:
        model=Position
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'no_of_seats':forms.NumberInput(attrs={'class':'form-control'}),
        }

class VotesForm(ModelForm):
    class Meta:
        model=Votes
        fields='__all__'
        widgets={
        }