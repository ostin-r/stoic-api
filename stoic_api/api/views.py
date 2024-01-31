import logging
from django.shortcuts import render
from django.http import JsonResponse
from api.models import Quote

# todo: add ability to get quote from author
# todo: get list of all authors
# todo: get list of all quotes
# todo: add POST / PUT / DELETE functions

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def quotes(request):
    response = {'success': True}
    if request.method == 'GET':
        body = request.GET
        logging.info(body)
        if body.get('daily', False):
            daily_quote = Quote.objects.get(is_daily=True)
            response.update({'quote': daily_quote.quote, 'author': daily_quote.author, 'source': daily_quote.source})
        elif body.get('random', False):
            random_quote = Quote.objects.order_by('?').first()
            response.update({'quote': random_quote.quote, 'author': random_quote.author, 'source': random_quote.source})
        else:
            pass # todo: get all quote
        # if the list gets big, update with more efficient method
        pass
    return JsonResponse(response)


# todo: add a function to update daily quote

