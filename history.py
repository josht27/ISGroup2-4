from catalog import models as cmod

class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        id_list = request.session.get('last5',[])

        request.last_five = []

        for i in id_list:
            request.last_five.append(cmod.Product.objects.get(id=i))


        response = self.get_response(request)
        request.session['last5'] = []

        for i in request.last_five:
            request.session['last5'].append(i.id)

        return response
