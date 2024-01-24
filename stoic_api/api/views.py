from django.shortcuts import render
from django.http import JsonResponse
from api.models import Quotes

# todo: add ability to get quote from author
# todo: get list of all authors
# todo: get list of all quotes
# todo: add POST / PUT / DELETE functions


def quotes(request):
    response = {'success': True}
    if request.method == 'GET':
        # if the list gets big, update with more efficient method
        random_quote = Quotes.objects.order_by('?').first()
        response.update({'quote': random_quote.quote, 'author': random_quote.author})
    return JsonResponse(response)

