from django import forms

from LoginApp.models import Register

class SignInForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ('FirstName', 'LastName',)