from django.urls import path
from api import views as api_views

urlpatterns = [
        path('', api_views.quotes)
    ]

