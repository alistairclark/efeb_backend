import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def checkout(request):
    cart_raw = request.POST.get("cart")

    if cart_raw is None:
        return HttpResponse("Borked")
    cart = json.loads(cart_raw)

    line_items = []
    for item_raw in cart:
        item = json.loads(item_raw)
        for _ in range(item.get("quantity")):
            line_items.append(
                {
                    "currency": "GBP",
                    "amount": int(float(item.get("price")) * 100),
                    "name": item.get("display_name"),
                }
            )

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url=request.build_absolute_uri(reverse("orders:order-success")),
            cancel_url=request.build_absolute_uri(reverse("orders:order-cancelled")),
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def order_success(request):
    return HttpResponse("Success")


def order_cancelled(request):
    return HttpResponse("Failed")
