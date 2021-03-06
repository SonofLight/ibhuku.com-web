from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Button, Reset
from crispy_forms.bootstrap import FormActions, PrependedText

from .models import IbkUser, Profile


class IbkUserSignUpForm(ModelForm):

	class Meta:
		model = IbkUser
		fields = ('name', 'email', 'password')
		fields_required = ('name')
		widgets = {
			'name': forms.TextInput(attrs={'id': 'signup_name'}),
			'email': forms.EmailInput(attrs={'id': 'signup_email'}),
			'password': forms.PasswordInput(attrs={'id': 'signup_password', 'placeholder': ' Enter Password'})
		}

	def clean_password(self):
		password = self.cleaned_data.get('password')
		if len(password) < 8:
			raise forms.ValidationError('Password must be at least 8 characters.')
		else:
			password_hashed =  make_password(password, salt='jRkSlAw7KZ')
			return password_hashed

	def __init__(self, *args, **kwargs):
		super(IbkUserSignUpForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'registerForm'
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
				PrependedText('name', "<span class='glyphicon glyphicon-user'></span>", placeholder="Name", active=True),
				PrependedText('email', "<span class='glyphicon glyphicon-envelope'></span>", placeholder="Email", active=True),
				PrependedText('password', "<span class='glyphicon glyphicon-lock'></span>", placeholder="Password", active=True),
				FormActions(
					Submit('submit', 'Submit', css_class ='btn btn-success btn-lg btn-block'),
					),
			)

class ResetActivationLinkForm(forms.Form):
	email = forms.EmailField(label='Email', max_length=255, required=True)

	def __init__(self, *args, **kwargs):
		super(ResetActivationLinkForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'resetLinkForm'
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
				PrependedText('email', "<span class='glyphicon glyphicon-envelope'></span>", placeholder="Email", active=True),
				FormActions(
					Submit('submit', 'Send Link', css_class ='btn btn-success btn-block'),
					),
			)
