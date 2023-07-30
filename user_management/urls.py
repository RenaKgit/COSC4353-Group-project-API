from django.urls import include, path
from .views import UserProfileCreate, GetFuelQuote


urlpatterns = [

    path('create-profile/', UserProfileCreate.as_view(), name='create-user'),
    path('quote-module/', GetFuelQuote.as_view(), name='quote-module'),]
