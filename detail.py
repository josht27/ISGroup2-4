from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod


@view_function
def process_request(request, prod:cmod.Product=None):

    product = cmod.Product.objects.get(id=prod.id)
    name = product.name

    for p in request.last_five:
        if product == p:
            request.last_five.remove(p)


    request.last_five.insert(0, product)

    while len(request.last_five) > 6:
        request.last_five.pop()

    context = {
        'prod': prod,
        'images': product.image_urls(),
        'name': name,
        
    }
    return request.dmp.render('detail.html', context)
