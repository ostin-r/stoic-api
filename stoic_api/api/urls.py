from django.urls import path
from api import views as api_views

urlpatterns = [
    path('v1/quotes/', api_views.quotes)
]

