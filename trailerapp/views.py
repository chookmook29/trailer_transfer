from django.shortcuts import render, redirect
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
