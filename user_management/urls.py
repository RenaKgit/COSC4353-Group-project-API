from django.urls import include, path
from .views import UserProfileCreate


urlpatterns = [

    path('create-profile/', UserProfileCreate.as_view(), name='create-user'),]