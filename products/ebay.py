from .serializers import TV_Serializer,Cams_Serializer,CarsElec_Serializer,Health_Serializer,VideoGames_Serializer,Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,Software_Serializer,Applinces_Serializer,Movies_Serializer,Office_Serializer
import requests
import json
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status


baseAddress = "http://localhost:8000/"

class EbayAPI():





    def ebayHealth(self,request):
        response = requests.get(baseAddress+"products/health/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems=0

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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Health_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
                            serializer.save()
                        else:
                            print("bad json")
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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










    def ebayToys(self,request):
        response = requests.get(baseAddress+"products/toys/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems=data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems=0

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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Toys_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
                            serializer.save()
                        else:
                            print("bad json")
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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




    def ebayAudio(self,request):
        response = requests.get(baseAddress+"products/audio/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"

            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Audio_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebayApplinces(self,request):
        response = requests.get(baseAddress+"products/applinces/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"

            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Applinces_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebayMovies(self,request):
        response = requests.get(baseAddress+"products/movies/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"


            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems=0

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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Movies_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebayOffice(self,request):
        response = requests.get(baseAddress+"products/office/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"




            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Office_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebaySoftware(self,request):
        response = requests.get(baseAddress+"products/software/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"




            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)

                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems = 0
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Software_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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




    def ebayVideo(self,request):
        response = requests.get(baseAddress+"products/video/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand']!= None:
                brand=unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii','ignore')
            else:
                brand="Brand Not Available"
            if item['SNR_Description'] !=None:
                description=item['SNR_Description']
            else:
                description=" Not Available"

            if item['SNR_ModelNo']!=None:

                model=item['SNR_ModelNo']
            else:
                model=" "
            if item['SNR_UPC']!=None:
                upc=item['SNR_UPC']
            else:
                upc="Not Available"
            if item['SNR_ImageURL'] !=None:

                img=item['SNR_ImageURL']
            else:
                img="Not Available"


            try:




                if model !=None:
                    response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                    data =json.loads(response.text)
                    #print(data)

                    if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                        totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                    else:
                        totalItems = 0

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
                            if img !=None:
                                request["SNR_ImageURL"] = img
                            else:
                                request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                            request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                            request["SNR_ModelNo"]=model
                            if itemm['itemId'][0]!=None:
                                request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                            if upc !=None:
                                request["SNR_UPC"]=upc
                            else:
                                request["SNR_UPC"] = "0000"
                            serializer = VideoGames_Serializer(data=request)
                            # print("bestbuy calling")
                            print(serializer)
                            if serializer.is_valid():
                                print "------"
                                serializer.save()
                            else:
                                print("bad json")
                                #return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

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
            except:
                print "exception"




    def ebaySmarthome(self,request):
        response = requests.get(baseAddress+"products/smarthome/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"


            try:


                if model !=None:
                    response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                            if img !=None:
                                request["SNR_ImageURL"] = img
                            else:
                                request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                            request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                            request["SNR_ModelNo"]=model
                            if itemm['itemId'][0]!=None:
                                request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                            if upc !=None:
                                request["SNR_UPC"]=upc
                            else:
                                request["SNR_UPC"] = "0000"
                            serializer = Smarthomes_Serializer(data=request)
                            # print("bestbuy calling")
                            # print(serializer)
                            if serializer.is_valid():
                                print "------"
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
            except:
                print "Pagination Error"




    def ebayCars(self,request):
        response = requests.get(baseAddress+"products/cars/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"




            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                # print(data)
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = CarsElec_Serializer(data=request)

                        # print("bestbuy calling")
                        print(serializer)
                        if serializer.is_valid():
                            print "------"
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






    def ebayCams(self,request):
        response = requests.get(baseAddress+"products/cams/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand'] != None:
                brand = unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii', 'ignore')
            else:
                brand = "Brand Not Available"
            if item['SNR_Description'] != None:
                description = item['SNR_Description']
            else:
                description = " Not Available"

            if item['SNR_ModelNo'] != None:

                model = item['SNR_ModelNo']
            else:
                model = " "
            if item['SNR_UPC'] != None:
                upc = item['SNR_UPC']
            else:
                upc = "Not Available"
            if item['SNR_ImageURL'] != None:

                img = item['SNR_ImageURL']
            else:
                img = "Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
                data =json.loads(response.text)
                #print(data)
                if 'paginationOutput' in data['findItemsAdvancedResponse'][0]:
                    totalItems = data['findItemsAdvancedResponse'][0]['paginationOutput'][0]['totalEntries'][0]
                else:
                    totalItems = 0


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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = Cams_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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






    def ebayTV(self,request):
        response = requests.get(baseAddress+"products/tv/models")
        data =json.loads(response.text)
    #    print(data)
        brand=""
        description=""
        model=""
        upc=""

        for item in data:
            #print(item['SNR_ModelNo'])
            if item['SNR_Brand']!= None:
                brand=unicodedata.normalize('NFKD', item['SNR_Brand']).encode('ascii','ignore')
            else:
                brand="Brand Not Available"
            if item['SNR_Description'] !=None:
                description=item['SNR_Description']
            else:
                description=" Not Available"

            if item['SNR_ModelNo']!=None:

                model=item['SNR_ModelNo']
            else:
                model=" "
            if item['SNR_UPC']!=None:
                upc=item['SNR_UPC']
            else:
                upc="Not Available"
            if item['SNR_ImageURL'] !=None:

                img=item['SNR_ImageURL']
            else:
                img="Not Available"



            if model !=None:
                response = requests.get("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=huzaifaz-ERecomme-PRD-008fa563f-8f5d310e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD=true&paginationInput.entriesPerPage=100&keywords="+model+"&itemFilter(0).name=Condition&itemFilter(0).value=New&itemFilter(1).name=sortOrder&itemFilter(1).value=CurrentPriceLowest")
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
                        if img !=None:
                            request["SNR_ImageURL"] = img
                        else:
                            request["SNR_ImageURL"] = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                        request["SNR_ProductURL"]=unicodedata.normalize('NFKD',itemm['viewItemURL'][0]).encode('ascii','ignore')
                        request["SNR_ModelNo"]=model
                        if itemm['itemId'][0]!=None:
                            request["SNR_SKU"]="EB"+str(itemm['itemId'][0])
                        if upc !=None:
                            request["SNR_UPC"]=upc
                        else:
                            request["SNR_UPC"] = "0000"
                        serializer = TV_Serializer(data=request)
                        # print("bestbuy calling")
                        # print(serializer)
                        if serializer.is_valid():
                            print "------"
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

