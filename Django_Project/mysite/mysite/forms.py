from django import forms

class Userform(forms.Form):
    Name=forms.CharField(label=False, widget=forms.TextInput(attrs={'class':'form-control my-1', 'placeholder':'Name'}))
    Phone=forms.CharField(label=False, widget=forms.NumberInput(attrs={'class':'form-control my-1', 'placeholder':'Phone'}))
    Email=forms.EmailField(label=False, widget=forms.EmailInput(attrs={'class':'form-control my-1', 'placeholder':'Email'}))
    Textarea = forms.DateField(label=False, widget=forms.Textarea(attrs={'class':'form-control my-1', 'rows':"3", 'placeholder':'Your Suggestion..'}))