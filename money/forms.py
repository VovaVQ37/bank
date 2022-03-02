from django.forms import ModelForm, HiddenInput

from .models import Transaction


class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        fields = (
            'sender',
            'receiver',
            'total',
            'date_time',
            'successful',
        )
        widgets = {
            'successful': HiddenInput(),
        }
