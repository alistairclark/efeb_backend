import json

from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

import stripe

from efeb_backend.products.models import Product
from efeb_backend.orders.choices import SUCCESS
from efeb_backend.orders.models import Order, OrderItem


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def checkout(request):
    post_data = request.POST
    cart_raw = post_data.get("cart")
    if cart_raw is None:
        return HttpResponse("No cart data received")

    cart = json.loads(cart_raw)

    order = Order.objects.create(
        customer_name=post_data.get("name"),
        address_line_1=post_data.get("address_line_1"),
        address_line_2=post_data.get("address_line_2"),
        city=post_data.get("city"),
        postcode=post_data.get("postcode"),
    )

    order.notify_admin()

    line_items = []
    for item in cart.values():
        data = item.get("data")
        quantity = item.get("quantity")

        product = Product.objects.get(slug=data.get("slug"))
        if product.stock_count < quantity:
            return HttpResponseBadRequest("Insufficient stock.")

        line_items.append(
            {
                "currency": "GBP",
                "amount": int(float(data.get("price")) * 100),
                "name": data.get("display_name"),
                "quantity": quantity,
            }
        )

        OrderItem.objects.create(product=product, order=order, quantity=quantity)

    checkout_session = stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        success_url=f"{settings.FRONTEND_URL}success/",
        cancel_url=f"{settings.FRONTEND_URL}cancelled/",
        client_reference_id=order.uuid,
    )

    return redirect(checkout_session.url, code=303)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")

    event = stripe.Webhook.construct_event(
        payload, sig_header, settings.STRIPE_WEBHOOK_SECRET_KEY
    )

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        order = Order.objects.get(uuid=session.get("client_reference_id"))
        order.status = SUCCESS
        order.email = session.get("customer_details", {}).get("email")
        order.decrement_stock()
        order.save()
        order.notify_customer()

    return JsonResponse({"message": "Success!"})
