from django.http import HttpResponse


def index(request):
    return HttpResponse('Скоро здесь будут объявления!')
