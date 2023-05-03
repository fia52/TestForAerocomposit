from django import forms

from .models import Currency


class ConverterForm(forms.Form):
    amount = forms.DecimalField(decimal_places=4)
    from_currency = forms.ModelChoiceField(queryset=Currency.objects.all())
    to_currency = forms.ModelChoiceField(queryset=Currency.objects.all())
