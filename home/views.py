from django.shortcuts import render
from home.forms import ContainerForm, PartForm
from django.http import HttpResponseRedirect, HttpResponse
from home.models import Container

def home(request):
    return render(request, "home.html")

def incoming(request):
    incomingContainers = Container.objects.all()
    context = {
        'incomingContainers': incomingContainers,
    }
    return render(request, 'incoming.html', context)

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
            part1 = form.cleaned_data['part1']
            qty1 = form.cleaned_data['qty1']

            part2 = form.cleaned_data['part2']
            qty2 = form.cleaned_data['qty2']

            part3 = form.cleaned_data['part3']
            qty3 = form.cleaned_data['qty3']

            part4 = form.cleaned_data['part5']
            qty4 = form.cleaned_data['qty5']

            part6 = form.cleaned_data['part6']
            qty6 = form.cleaned_data['qty6']

            part7 = form.cleaned_data['part7']
            qty7 = form.cleaned_data['qty7']

            part8 = form.cleaned_data['part8']
            qty8 = form.cleaned_data['qty8']

            part9 = form.cleaned_data['part9']
            qty9 = form.cleaned_data['qty9']

            part10 = form.cleaned_data['part10']
            qty10 = form.cleaned_data['qty10']
            
            part11 = form.cleaned_data['part11']
            qty11 = form.cleaned_data['qty11']

            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/containers/thankyou/')
    else:
        form = ContainerForm()
    return render(request, 'containers.html', {'form': form})

def cthankyou(request):
    return render(request, 'cthankyou.html')
