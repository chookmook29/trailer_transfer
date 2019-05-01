from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Door
from .forms import DoorForm


def main(request):
    all_doors = Door.objects.order_by('door_number')
    return render(request, 'index.html', {'all_doors': all_doors})


def empty(request, door_id):
    item = Door.objects.get(pk=door_id)
    item.status = 'Empty'
    item.save()
    return redirect('main')


def loaded(request, door_id):
    item = Door.objects.get(pk=door_id)
    item.status = 'Loaded'
    item.save()
    return redirect('main')


def in_progress(request, door_id):
    item = Door.objects.get(pk=door_id)
    item.status = 'In Progress'
    item.save()
    return redirect('main')


def clear(request, door_id):
    item = Door.objects.get(pk=door_id)
    item.trailer_number = 'No Trailer'
    item.status = 'None'
    item.save()
    return redirect('main')


def pushback(request, door_id):
    item = Door.objects.get(pk=door_id)
    item.status = 'Pushback'
    item.save()
    return redirect('main')

def edit(request, door_id):
    if request.method == 'POST':
        item = Door.objects.get(pk=door_id)
        form = DoorForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        item = Door.objects.get(pk=door_id)
        return render(request, 'edit.html', {'item': item})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return redirect('main')
    else:
        return render(request, 'login.html')
