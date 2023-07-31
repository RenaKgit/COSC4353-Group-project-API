from django.shortcuts import render
from .models import UserInfo
from rest_framework import generics, status
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


states = [
    'al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga',
    'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md',
    'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj',
    'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc',
    'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy'
]

class UserProfileCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new client profile

    queryset = UserInfo.objects.all(),
    serializer_class = UserSerializer

class GetFuelQuote(APIView):

    def post(self, request):
        
        
        #grabs state id from models.py
        def getstatefactor(state):
            if(state == "tx"):
                return 0.02
            else:
                return 0.01
        
        
        gallonsrequested = request.data.get('gallons_requested')
        location = request.data.get('location')

        #some error handling 
        if location is None or gallonsrequested is None: 
            return Response({
           "Error": "Missing Values"
            },status = status.HTTP_400_BAD_REQUEST
            )  
        if location not in states:
            return Response({
           "Error": f"{location} is not a state"
            },status = status.HTTP_400_BAD_REQUEST
            )  
        
        #start calculations 
        statefactor  = getstatefactor(location)
        ratehistory = 0.01 #needs function to returns this 
        priceGallon = 1.50 # constant 
        profitFactor = 0.1 # constant 

        total = 0

        if gallonsrequested < 1000:
            gallonsFactor = 0.03
            margin = priceGallon * (statefactor -ratehistory + gallonsFactor + profitFactor)
            suggestedprice = priceGallon + margin
            total = gallonsrequested * suggestedprice
             
        else:
            gallonsFactor = 0.02
            margin = priceGallon * (statefactor -ratehistory + gallonsFactor + profitFactor)
            suggestedprice = priceGallon + margin
            print(margin, suggestedprice)
            total = gallonsrequested * suggestedprice

        return Response({

            "suggested": suggestedprice,
=======

           "total": total
       },status = status.HTTP_200_OK
       ) 
    

            



