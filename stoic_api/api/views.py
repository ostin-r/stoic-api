from django.shortcuts import render
from django.http import JsonResponse


def quotes(request):
    response = {'success': True}
    return JsonResponse(response)

