from django.shortcuts import render
from django.http import HttpResponse
from .models import Party

def index(request):

    all_parties = Party.objects.all()
    for p in all_parties:
        print(p.symbol)
    context = {
        'all_parties': all_parties
    }
    return render(request, 'home/index.html', context)


def profile(request, pk=None):

    if pk:
        user = User.objects.get(pk=pk)
        # print(user.username)
    else:
        user = request.user

    context = {
        'party_name': '',
        'party_image_path': '',
        'transactions': [],
    }

    return render(request, 'account/profile.html', context)