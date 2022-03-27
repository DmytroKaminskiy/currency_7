from django import forms

from currency.models import Rate, ContactUs


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('type', 'source', 'buy', 'sale')


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('subject', 'email', 'message_body')
