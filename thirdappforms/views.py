from django.shortcuts import render
from . import forms

# Create your views here.


def form_example(request):
    form = forms.thirdform()
    formss = {'form': form}

    if request.method == 'POST':
        form = forms.thirdform(request.POST)

        if form.is_valid():
            print('Validation success')
            print("Name: "+form.cleaned_data['name'])

    return render(request, 'form_ex.html', context=formss)
