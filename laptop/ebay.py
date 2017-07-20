__author__ = 'Amad'
import unicodedata


from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import Laptop_Serializer
from ebaysdk.finding import Connection as finding
import requests
import json
class EbayAPI():
    def ebayLaptops(self,request):
        response = requests.get("https://djangoshopnroar.herokuapp.com/laptop/getModels")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            brand=unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii','ignore')
            description=item['SNR_Description']
            model=item['SNR_ModelNo']
            upc=item['SNR_UPC']
            img=item['SNR_ImageURL']




            response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+item['SNR_ModelNo']+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
            data =json.loads(response.text)
            #print(data)
            totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
            if int(totalItems) > 0:
                # print("amad")
                # print(totalItems)
                # print(model)


                for itemm in data['findItemsAdvancedResponse'][0]['searchResult'][0]['item']:
                    request["SNR_Price"]=unicodedata.normalize('NFKD', itemm['sellingStatus'][0]['currentPrice'][0]['__value__']).encode('ascii','ignore')
                    request["SNR_Brand"]=brand
                    request["SNR_Available"]="Ebay"
                    request["SNR_Description"]=description
                    request["SNR_Title"]=unicodedata.normalize('NFKD', itemm['title'][0]).encode('ascii','ignore')
                    request["SNR_ImageURL"] = img
                    request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                    request["SNR_ModelNo"]=model
                    request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                    request["SNR_UPC"]=upc
                    serializer = Laptop_Serializer(data=request)
                    # print("bestbuy calling")
                    # print(serializer)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        print("bad json")
                    break
                else:
                    continue

                    # print(item['title'][0])
                    # print(item['itemId'][0])
                    # print(item['galleryURL'][0])
                    # print(item['viewItemURL'][0])
                    #
                    # print(item['sellingStatus'][0]['currentPrice'][0]['__value__'])
                    break


    def search(data):
        if data["company_SNR"].lower() == "lenovo" and data["series_SNR"].lower() == 'g':
            query = data["company_SNR"] + ' ' + data["series_SNR"]+data["model_SNR"]
        else:
            query = data["company_SNR"] + ' ' + data["series_SNR"] + ' ' + data["model_SNR"]

        api = finding(appid='huzaifaz-ERecomme-PRD-008fa563f-8f5d310e', debug=True)
        api.execute('findItemsAdvanced', {
                                            'keywords': query,
                                            'categoryId': ['175672','177', '111422'],
                                            'sortOrder': 'PricePlusShippingLowest',
                                            })


        #'itemFilter': [
                          #{'name': 'sortOrder', 'value': 'PricePlusShippingLowest'}
                      #],

        #'categoryId':[{'name': 'laptop & Netbooks', 'value': '175672'},
                      #{'name': 'Apple laptop', 'value': '111422'},
                      #{'name': 'PC laptop & Netbooks', 'value': '177'}],

        #CurrentPriceHighest

        dictstr = api.response.dict()
        #found = fortest.filterProducts(query,dictstr)

        if len(dictstr['searchResult']['item'])>0:

            for item in dictstr['searchResult']['item']:
                if item['condition']['conditionDisplayName'] != "For parts or not working" and query.lower() in item['title'].lower():
                    #myval=item['itemId']
                    #title=item['title']
                    #print title
                    data["price_SNR"]= item['sellingStatus']['convertedCurrentPrice']['value']
                    data["condition_SNR"]= item['condition']['conditionDisplayName']
                    data["link_SNR"]= item['viewItemURL']
                    data["CompleteName_SNR"]=item['title']
                    data["Available_SNR"]="EBAY"

                    serializer = Laptop_Serializer(data=data)

                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                    break
        else:
            print "Ebay Product not found"