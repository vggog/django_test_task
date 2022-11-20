from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import Item


def index():
    return HttpResponse(
        'Hello, welcome to the home page of the test task.'
    )


def item(request, item_id: int):
    try:
        product = Item.objects.get(
            id=item_id,
        )
    except Item.DoesNotExist:
        return HttpResponseNotFound(
            'Item not found.'
        )

    return render(
        request,
        'buy.html',
        context={
            'item_id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
        },
    )
