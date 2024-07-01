from django.shortcuts import render
from .models import Oakil

# Create your views here.
def home(request):
    contact = Oakil.objects.all()

    context = {
        'contact':contact
    }


    return render(request, 'masud/home.html',context)


def detail(request, id):
    contact = Oakil.objects.get(id= id)
    print(contact)

    context = {
        'contact':contact
    }



    return render(request, 'masud/detail.html', context)

