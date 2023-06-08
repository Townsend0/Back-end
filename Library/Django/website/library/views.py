from django.shortcuts import render, redirect
from .forms import BookForm
from django.contrib import messages
from .models import BookData

def home(request):
    return render(request, 'index.html', {'books': BookData.objects.all()})


def add(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if int(request.POST['rating']) not in range(11):
            messages.error(request, 'Please enter a number between 0 and 10')
        elif form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'add.html', {'form': form })