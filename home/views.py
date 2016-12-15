from django.shortcuts import render
from home.forms import ContainerForm, PartForm
from django.http import HttpResponseRedirect, HttpResponse


def home(request):
    return render(request, "home.html")

def incoming(request):

    return render(request, 'incoming.html')

def ithankyou(request):
    return render(request, 'ithankyou.html')

def outgoing(request):
    return render(request, "outgoing.html")

def othankyou(request):
    return render(request, 'othankyou.html')

def containers(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            containerNumber = form.cleaned_data['containerNumber']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/containers/thankyou/')
    else:
        form = ContainerForm()
    return render(request, 'containers.html', {'form': form})

def cthankyou(request):
    return render(request, 'cthankyou.html')
