from django.shortcuts import render
from .forms import ReserveTableForm


def reserve_table(request):

    reserve_form = ReserveTableForm()
    if request.method == 'GET':
        reserve_form = ReserveTableForm(request.GET)
        if reserve_form.is_valid():
            reserve_form.save()
    context = {'form': reserve_form}

    return render(request, 'reservation.html', context)
