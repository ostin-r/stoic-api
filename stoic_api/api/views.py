import logging
from django.http import JsonResponse
from django.db import models 
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
            all_quotes = Quote.objects.all()
            response['quotes'] = []
            for quote in all_quotes:
                formatted_quote = {
                        'quote': quote.quote, 
                        'author': quote.author, 
                        'source': {
                            'title': quote.source.title, 
                            'isbn': quote.source.isbn, 
                            'authors': []
                        }
                    }
                for author in quote.source.authors.all():
                    formatted_quote['source']['authors'].append(author.name)
                response['quotes'].append(formatted_quote)
    else:
        response.update({'success': False, 'message': 'Request type not supported for quotes'})
    return JsonResponse(response)


