from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
import stripe

from .models import Item
from . import services
from . import settings


def index():
    return HttpResponse(
        'Hello, welcome to the home page of the test task.'
    )


def item(request, item_id: int):
    """
    View for get page with info about item and get "buy" button.
    """
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
            'price': services.get_price_in_dollars(
                price_in_cents=product.price
            ),
        },
    )


def buy(request, item_id):
    """
    View for get Stripe Session ID for pay chosen item
    """
    try:
        product = Item.objects.get(
            id=item_id,
        )
    except Item.DoesNotExist:
        return HttpResponseNotFound(
            'Item not found.'
        )

    stripe.api_key = settings.STRIPE_API_KEY
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': product.price_id,
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=settings.DOMAIN + '/buy_complete_success',
        cancel_url=settings.DOMAIN + '/buy_canceled',
    )

    return JsonResponse({'session_id': checkout_session.id})


def buy_success_complete(request):
    """
    Purchase complete page.
    """
    return render(
        request,
        'success.html',
    )


def buy_canceled(request):
    """
    Purchase cancel page.
    """
    return render(
        request,
        'cancel.html',
    )
