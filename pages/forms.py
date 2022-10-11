from django import forms
from django.forms import EmailInput, TextInput

class ContactForm(forms.Form):
    submit_name = forms.CharField(label='',widget=forms.TextInput(attrs={
							'placeholder':'Your Name',
							#'style': 'width: 300px;',
							'class': 'input w-full bg-black border-b bg-opacity-0 text-white px-0 py-4 mb-4 tm-border-gold'}), required=False)
    submit_email = forms.EmailField(label='',widget=forms.EmailInput(attrs={
                                                                'placeholder':'Your Email',
                                                                #'style': 'width: 300px;',
                                                                'class': 'input w-full bg-black border-b bg-opacity-0 text-white px-0 py-4 mb-4 tm-border-gold'}), required=False)
    submit_number = forms.CharField(label='',widget=forms.TextInput(attrs={
                                                                'placeholder':'Your Number',
                                                                #'style': 'width: 300px;',
                                                                'class': 'input w-full bg-black border-b bg-opacity-0 text-white px-0 py-4 mb-4 tm-border-gold'}), required=False)



    submit_message = forms.CharField(label='',widget=forms.Textarea(attrs={
							'placeholder':'Your Message',
							#'style':'width: 300px;',
                                                        'rows':6,
							'class': 'form-control'}), required=False)
