from re import M


multiple_items_json = {
    "cart": '{"canyon":{"data":{"manufacturer":{"display_name":"Electro-Harmonix","slug":"electro-harmonix"},"categories":[{"display_name":"Delay","slug":"delay"},{"display_name":"Looping","slug":"looping"}],"display_name":"Canyon","price":"60.00","picture":"https://efeb-backend-media.s3.amazonaws.com/electro_harmonix_canyon_delay_and_looper_1325575.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQZLOUKRABQNNZKCL%2F20220713%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220713T154219Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=842567eaa52b7ee4155cdaa4125d6c073eaa65f83f02510115bc22bd0a3c32a4","stock_count":1,"description":"Multi-function delay pedal","links":"https://example.com","slug":"canyon"},"quantity":1},"metal-zone-mt-2":{"data":{"manufacturer":{"display_name":"Boss","slug":"boss"},"categories":[{"display_name":"Distortion","slug":"distortion"}],"display_name":"Metal Zone MT-2","price":"45.00","picture":"https://efeb-backend-media.s3.amazonaws.com/bomt2-xl-01.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQZLOUKRABQNNZKCL%2F20220713%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220713T154229Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=06e218bb2eee2ea63b9760cb048cea98d39f01ef5ddacd7479e2ed4c5be6a159","stock_count":1,"description":"Boss Metal Zone MT-2","links":"https://boss.com","slug":"metal-zone-mt-2"},"quantity":1}}'
}

multiples_of_one_item_json = {
    "cart": '{"metal-zone-mt-2":{"data":{"manufacturer":{"display_name":"Boss","slug":"boss"},"categories":[{"display_name":"Distortion","slug":"distortion"}],"display_name":"Metal Zone MT-2","price":"45.00","picture":"https://efeb-backend-media.s3.amazonaws.com/bomt2-xl-01.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQZLOUKRABQNNZKCL%2F20220713%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220713T155746Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d5ce34d51aa63d2ebd59306af38c715c48b13a3b5cd7df2b02626a24a6be072d","stock_count":10,"description":"Boss Metal Zone MT-2","links":"https://boss.com","slug":"metal-zone-mt-2"},"quantity":4}}'
}

insufficient_stock_data = {
    "cart": '{"metal-zone-mt-2":{"data":{"manufacturer":{"display_name":"Boss","slug":"boss"},"categories":[{"display_name":"Distortion","slug":"distortion"}],"display_name":"Metal Zone MT-2","price":"45.00","picture":"https://efeb-backend-media.s3.amazonaws.com/bomt2-xl-01.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQZLOUKRABQNNZKCL%2F20220713%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220713T155746Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=d5ce34d51aa63d2ebd59306af38c715c48b13a3b5cd7df2b02626a24a6be072d","stock_count":10,"description":"Boss Metal Zone MT-2","links":"https://boss.com","slug":"metal-zone-mt-2"},"quantity":11}}'
}

stripe_webhook_data = {
    "data": {
        "object": {
            "id": "cs_test_a1XELIs0SnK0nSYp1AVPrQC1m19Tr8kss7pSCE2S131Gucv9RsZx8uGG0U",
            "object": "checkout.session",
            "after_expiration": None,
            "allow_promotion_codes": None,
            "amount_subtotal": 4500,
            "amount_total": 4500,
            "automatic_tax": {"enabled": False, "status": None},
            "billing_address_collection": None,
            "cancel_url": "http://localhost:3000/cancelled/",
            "client_reference_id": "9f0bcfe8-94c1-4352-a109-542c1adb3701",
            "consent": None,
            "consent_collection": None,
            "currency": "gbp",
            "customer": "cus_M3UaqtdMolXZFg",
            "customer_creation": "always",
            "customer_details": {
                "address": {
                    "city": None,
                    "country": "GB",
                    "line1": None,
                    "line2": None,
                    "postal_code": "G11 5NU",
                    "state": None,
                },
                "email": "alistairclark89@gmail.com",
                "name": "MR A CLARK",
                "phone": None,
                "tax_exempt": "none",
                "tax_ids": [],
            },
            "customer_email": None,
            "expires_at": 1657874451,
            "livemode": False,
            "locale": None,
            "metadata": {},
            "mode": "payment",
            "payment_intent": "pi_3LLNbLKBGN6jeKlL1TOPuInw",
            "payment_link": None,
            "payment_method_options": {},
            "payment_method_types": ["card"],
            "payment_status": "paid",
            "phone_number_collection": {"enabled": False},
            "recovered_from": None,
            "setup_intent": None,
            "shipping": None,
            "shipping_address_collection": None,
            "shipping_options": [],
            "shipping_rate": None,
            "status": "complete",
            "submit_type": None,
            "subscription": None,
            "success_url": "http://localhost:3000/success/",
            "total_details": {
                "amount_discount": 0,
                "amount_shipping": 0,
                "amount_tax": 0,
            },
            "url": None,
        },
    },
    "type": "checkout.session.completed",
}
