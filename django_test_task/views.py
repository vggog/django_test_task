from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Hello, welcome to the home page of the test task.')


def item(request, item_id: int):
    return render(
        request,
        'buy.html',
        context={
            'item_id': item_id,
        },
    )
