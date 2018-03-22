from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

@view_function
def process_request(request, product:cmod.Product=None):

    for p in request.last_five:
        if product == p:
            request.last_five.remove(p)

    request.last_five.insert(0, product)

    while len(request.last_five) > 6:
        request.last_five.pop()

    context = {
        'product': product,
        'images': product.image_urls(),
        'first': product.image_url(),
    }

    return request.dmp.render('detail.html', context)
