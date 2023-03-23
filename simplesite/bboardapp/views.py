from django.shortcuts import render
from .models import Bb


def index(request):
    bbs = Bb.objects.all()
    context = {'bbs': bbs}
    return render(request, 'bboardapp/index.html', context)
