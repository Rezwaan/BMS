__author__ = 'Amad'
import json
from . models import Trends
from . serializer import TrendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status

from ebaysdk.merchandising import Connection as Merchandising
from ebaysdk import exception
class EbayAPI():

    def AddTrend(self,request):
        print("uddin")
        api = Merchandising(appid="huzaifaz-ERecomme-PRD-008fa563f-8f5d310e")
        try:

            api = Merchandising(appid="huzaifaz-ERecomme-PRD-008fa563f-8f5d310e")
            response = api.execute('getTopSellingProducts', {'maxResults': 10})
            print(response.dict())
            #print(response.reply)
            dictstr=response.dict()

            for item in dictstr['productRecommendations']['product']:

                request["SNR_Title"]=item['title'];
                request["SNR_PriceMin"]=item['priceRangeMin']['value'];
                request["SNR_PriceMax"]=item['priceRangeMax']['value'];
                request["SNR_ProductURL"]=( item['productURL']);
                request["SNR_AvailableAt"]="Ebay"
                request["SNR_Type"] = "Trending";
                request["SNR_Category"] = "mobile+wearable+laptop";

                #
                # print( item['productURL']);
                # print(item['title']);
                # print(item['priceRangeMin']['value']);

                if 'imageURL' in item:

                    # print(item['imageURL'])
                    request["SNR_ImageURL"]=item['imageURL'];



                else:
                    continue


                serializer = TrendsSerializer(data=request)
                if serializer.is_valid():
                    serializer.save()
                else:

                 print "bad json"



        except exception as e:

            print("exception")
            print(e)
            print(e.response.dict())

