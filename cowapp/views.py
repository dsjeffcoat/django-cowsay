from django.shortcuts import render
from cowapp.models import CowText
from cowapp.forms import CowForm
import subprocess as sp
# Create your views here.


def index(request):
    cow_moo = ''
    if request.method == 'POST':
        form = CowForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CowText.objects.create(
                text=data.get('text')
            )
            cow_moo = sp.run(['cowsay', data.get('text')],
                             capture_output=True, text=True)
            return render(request, 'index.html', {'form': CowForm, 'cow_moo': cow_moo.stdout})
    form = CowForm()
    return render(request, 'index.html', {'form': CowForm, 'cow_moo': cow_moo})


def moo_history(request):
    past_moos = []
    moo_list = CowText.objects.all().order_by('-pk')[:10]
    moo_count = len(moo_list)
    if moo_count >= 10:
        for i in range(0, 10):
            past_moos.append([i+1, moo_list[i].text])
    else:
        for i in range(0, moo_count):
            past_moos.append([i+1, moo_list[i].text])
    return render(request, 'history.html', {'moo_list': moo_list})
