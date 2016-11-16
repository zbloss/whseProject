from django.shortcuts import render
from home.forms import IncomingForm

def home(request):
    return render(request, "home.html")

def incoming(request):
    if request.method == 'POST':
        form = IncomingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            instance = form.save(commit=False)
            instance.save()
            print("instance it was saved")
            return HttpResponseRedirect('/')
    else:
        form = IncomingForm()
    return render(request, 'incoming.html', {'form': form})

def addIncoming(request):
    if request.method == 'POST':
        form = IncomingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            instance = form.save(commit=False)
            instance.save()
            print("instance it was saved")
            return HttpResponseRedirect('/')
    else:
        form = IncomingForm()
    return render(request, 'incoming.html', {'form': form})


def outgoing(request):
    return render(request, "outgoing.html")
