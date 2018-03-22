from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        prods = request.session.get('lastFive', [])
        request.last_five = []

        for item in prods:
            request.last_five.append(cmod.Product.objects.get(id=item))

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        request.session['lastFive'] = []

        for item in request.last_five:
            request.session['lastFive'].append(item.id)

        return response
