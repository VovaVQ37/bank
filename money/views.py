from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Account
from .forms import TransactionForm


def send(request):
    if not request.user.is_authenticated:
        return render(request, 'money/auth.html', {})
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print(request.POST)
            print('sender=', request.POST.get('sender'))
            sender = get_object_or_404(Account, pk=request.POST.get('sender'))
            receiver = get_object_or_404(Account, pk=request.POST.get('receiver'))
            successful = True
            if sender.total >= int(request.POST.get('total')):
                sender.total -= int(request.POST.get('total'))
                receiver.total += int(request.POST.get('total'))
                sender.save()
                receiver.save()
            else:
                successful = False
            form.successful = successful
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = TransactionForm()
    return render(request, 'money/send.html', {'form': form})


def success(request):
    return render(request, 'money/success.html', {})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/send/')
        else:
            message = "Wrong login and/or password"
            return HttpResponseRedirect('/auth/', kwargs={'message': message})

    return render(request, 'money/auth.html', {'message': ''})
