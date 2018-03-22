from catalog import models as cmod


class LastFiveMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        id_list = request.session.get('lastfive', [])

        request.last_five = []
        for stuff in id_list:
            request.last_five.append(cmod.Product.objects.get(id=stuff))

        response = self.get_response(request)
        request.session['lastfive']=[]

        for item in request.last_five:
            request.session['lastfive'].append(item.id)


        return response
