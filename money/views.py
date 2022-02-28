from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from .models import Account, Transaction
from .forms import TransactionForm


def send(request):
    TransactionFormSet = modelformset_factory(Transaction, form=TransactionForm)
    if request.method == 'POST':
        formset = TransactionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            forms = formset.save(commit=False)
            for i, form in enumerate(forms):
                print(request.POST)
                print('sender=', request.POST.get('form-' + str(i) + '-sender'))
                sender = get_object_or_404(Account, pk=request.POST.get('form-' + str(i) + '-sender'))
                receiver = get_object_or_404(Account, pk=request.POST.get('form-' + str(i) + '-receiver'))
                successful = True
                if sender.total >= int(request.POST.get('form-' + str(i) + '-total')):
                    sender.total -= int(request.POST.get('form-' + str(i) + '-total'))
                    receiver.total += int(request.POST.get('form-' + str(i) + '-total'))
                    sender.save()
                    receiver.save()
                else:
                    successful = False
                form.successful = successful
                form.save()
            return HttpResponseRedirect('/success/')
    else:
        formset = TransactionFormSet()
    print(formset)
    return render(request, 'money/send.html', {'formset': formset})


def success(request):
    return render(request, 'money/success.html', {})
