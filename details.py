from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math


@view_function
def process_request(request, prod:cmod.Product=None,):

    # if prod.TITLE == 'Bulk':
    #     qty = prod.quantity
    #
    # else:
    #     qty = 0;


    for p in request.last_five:
        if prod == p:
            request.last_five.remove(p)

    request.last_five.insert(0, prod)

    while len(request.last_five)> 6:
        request.last_five.pop()


    context = {

        'prod':prod,
        'images':prod.image_urls(),
        'first':prod.image_url(),

    }


    return request.dmp.render('details.html', context)
