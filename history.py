from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        request.last_five = []
        for pid in request.session.get('lastfive', []):
            request.last_five.append(cmod.Product.objects.get(id=pid))

        # for item in idlist:
        #     request.last_five.append(item)
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # Get the list of product ids from the session. request.session.get()
        # convert the product ids into a list of product objests.
        # request.last_five = [ ... ]

    # if they are on detail.py
        # product variable
        ## remove if already in the list

        # request.last_five.insert(0, product)
        # if len > 6 items, remove the last


            # in catalog/templates/app_base.htm:
                #for loop through request.last_five - print the thumbnails

            # After the request (in middleware) catalog/history.py (__call__method):
                # request.session ['...'] = list of ids


        response = self.get_response(request)

        pids=[]
        for item in request.last_five[:6]:
            pids.append(item.id)
        request.session['lastfive'] = pids



        return response
