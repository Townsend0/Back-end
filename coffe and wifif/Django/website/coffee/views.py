from django.shortcuts import redirect, render
from .forms import CafeForm
from .models import CafeData
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, 'index.html')

def show(request):
    return render(request, 'cafes.html', {'cafes': CafeData.objects.all()})

def add(request):
    form = CafeForm()
    if request.method == 'POST':
        form = CafeForm(request.POST)
        try:
            CafeData.objects.get(name = form.data['name'])
            messages.error(request, 'The cafe exists already')
        except ObjectDoesNotExist:
            if form.is_valid():
                form.save()
                return redirect('home')
    return render(request, 'add.html', {'form': form})