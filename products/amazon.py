
from amazonproduct import API
import lxml.etree
import unicodedata
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .serializers import Audio_Serializer, CarsElec_Serializer,Software_Serializer,TV_Serializer,Movies_Serializer,Toys_Serializer,Cams_Serializer,Office_Serializer,VideoGames_Serializer,Smarthomes_Serializer,Applinces_Serializer
from ebaysdk.finding import Connection as finding
from lxml import objectify
import time


AWS_KEY = 'AKIAIHUQ37KJ3BJDWHXA'
SECRET_KEY = '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'

api = API(AWS_KEY, SECRET_KEY, 'us')

class AmazonAPI():

    def amazonAppliances(self,request):
        listCatagories = ['3737671', '267554011', '2632820011', '2242350011', '2686378011', '2686328011', '495362',
                          '678542011', '3741261', '3741271', '3737601', '3741331', '680343011', '267555011',
                          '2399939011', '510240', '510240', '289935', '3741181', '3741441', '3741411', '3741361',
                          '289913', '510182', '3741451', '510106', '3741481', '2399955011', '2383576011', '3741521']
        for category in listCatagories:
            try:

                for data in api.item_search('Electronics', BrowseNode=category, Sort='-price',
                                            ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:
                        request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        price = data.ItemAttributes.ListPrice.FormattedPrice
                        price = price[1:]
                        request["SNR_Price"] = float(price)

                    except:

                        try:
                            request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                        except:
                            request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Applinces_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages
            except:
                print "Error"




    def amazonAudio(self,request):

        # get all books from result set and
        # print author and title


        for data in api.item_search('Electronics', BrowseNode='172563', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"] ="No Brand"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages



        for data in api.item_search('Electronics', BrowseNode='322215011', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

        for data in api.item_search('Electronics', BrowseNode='3236443011', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages





        for data in api.item_search('Electronics', BrowseNode='172550', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages




        for data in api.item_search('Electronics', BrowseNode='172552', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages


        for data in api.item_search('Electronics', BrowseNode='667846011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Electronics', BrowseNode='13308581', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages





        for data in api.item_search('Electronics', BrowseNode='3236449011', Sort='-price',
                                    ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Audio_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

    def amazonCarsElectronics(self,request):

        # get all books from result set and
        # print author and title

        for data in api.item_search('Automotive', BrowseNode='15710351', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Automotive', BrowseNode='2204830011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Automotive', BrowseNode='15857511', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Automotive', BrowseNode='15857501', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)






        for data in api.item_search('Automotive', BrowseNode='15706941', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Automotive', BrowseNode='15706571', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Automotive', BrowseNode='2230642011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Electronics', BrowseNode='1077068', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(2)


            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:
                request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = CarsElec_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




    def amazonSoftware(self,request):

        # get all books from result set and
        # print author and title



        for data in api.item_search('Software', BrowseNode='229540', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Software', BrowseNode='229614', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Software', BrowseNode='229667', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='229545', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Software', BrowseNode='229672', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Software', BrowseNode='497024', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Software', BrowseNode='229653', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='229637', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='1294826011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Software', BrowseNode='229563', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='229548', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='229677', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='229535', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Software', BrowseNode='229534', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Software', BrowseNode='497026', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Software', BrowseNode='497022', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Software_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



    def amazonTV(self,request):

        # get all books from result set and
        # print author and title




        for data in api.item_search('Electronics', BrowseNode='3213025011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Electronics', BrowseNode='3213027011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Electronics', BrowseNode='3213035011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Electronics', BrowseNode='352696011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='281056', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='1286610011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='1288718011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='400080', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='3230976011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='578960', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='172659', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)






        for data in api.item_search('Electronics', BrowseNode='172669', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='3213034011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Electronics', BrowseNode='1266092011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = TV_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





    def amazonToys(self,request):

        # get all books from result set and
        # print author and title


        for data in api.item_search('Toys', BrowseNode='166508011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166118011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166309011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166316011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166164011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166220011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='165993011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='3226142011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='276729011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='165993011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166210011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166269011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166326011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166027011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='1266203011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166333011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166359011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Toys', BrowseNode='166092011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Toys', BrowseNode='166461011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Toys', BrowseNode='166420011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Toys', BrowseNode='256994011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Toys', BrowseNode='166310011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Toys', BrowseNode='166224011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Toys', BrowseNode='196601011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Toys', BrowseNode='166057011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Toys', BrowseNode='165993011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Electronics', BrowseNode='165793011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Toys_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




    def amazonMovies(self,request):

        # get all books from result set and
        # print author and title



        for data in api.item_search('DVD', BrowseNode='2625374011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Movies_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Electronics', BrowseNode='165793011', Sort='-price',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Movies_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





    def amazonCams(self,request):

        # get all books from result set and
        # print author and title


        for data in api.item_search('Photo', BrowseNode='499158',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3347771',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='297842',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='499170',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3168051',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='281063',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='4993282',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='499262', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3346401', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='172447', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='699138011', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='525898', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3349701', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3347871', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3117830011', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3346261', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='172450', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3348291', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3443921', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='196569011', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3349781', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='14015071', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3348211', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Photo', BrowseNode='525464',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Photo', BrowseNode='14241331',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


                for data in api.item_search('Photo', BrowseNode='14241151', ResponseGroup='ItemAttributes,Images',
                                            limit=1000, AssociateTag='bpl001-20'):
                    time.sleep(3)

                    # print(objectify.dump(data))
                    request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
                    try:
                        request["SNR_Title"] = str(data.ItemAttributes.Title)
                    except:
                        request["SNR_Title"] = "No Title"

                    try:

                        request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

                    except:
                        request["SNR_ModelNo"] = "00"

                    try:

                        request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

                    except:
                        request["SNR_SKU"] = "00"

                    try:

                        request["SNR_Description"] = str(data.ItemAttributes.Feature)

                    except:
                        request["SNR_Description"] = "Please visit site to see description"

                    try:
                        request["SNR_Brand"] = str(data.ItemAttributes.Brand)

                    except:

                        try:
                            request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                        except:
                            request["SNR_Brand"] = "None"

                    try:

                        request["SNR_ImageURL"] = str(data.LargeImage.URL)

                    except:

                        try:
                            request["SNR_ImageURL"] = str(data.MediumImage.URL)
                        except:
                            try:
                                request["SNR_ImageURL"] = str(data.SmallImage.URL)
                            except:
                                request["SNR_ImageURL"] = None

                    try:

                        request["SNR_UPC"] = str(data.ItemAttributes.UPC)

                    except:
                        request["SNR_UPC"] = "000"

                    try:

                        price = data.ItemAttributes.ListPrice.FormattedPrice
                        price = price[1:]
                        request["SNR_Price"] = float(price)

                    except:

                        try:
                            request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                        except:
                            request["SNR_Price"] = str(0)

                    request["SNR_Available"] = "Amazon"

                    serializer = Cams_Serializer(data=request)
                    print "done"
                    # print serializer


                    if serializer.is_valid():
                        print "------------------------"

                        serializer.save()
                    else:
                        print "bad jason"
                        print serializer.errors
                        print serializer.error_messages

                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='14241441',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3426471',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3350301',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3350171',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3350211',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Photo', BrowseNode='3350181',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='562261011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='172427',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Photo', BrowseNode='172444',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3017971',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3017961',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='172441',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='499108',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='291226',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Photo', BrowseNode='51547011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)





        for data in api.item_search('Photo', BrowseNode='14015021',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)






        for data in api.item_search('Photo', BrowseNode='754486',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




        for data in api.item_search('Photo', BrowseNode='502394',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Photo', BrowseNode='2476680011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='3017941',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='2476681011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('Photo', BrowseNode='330405011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('Photo', BrowseNode='502394',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        for data in api.item_search('Photo', BrowseNode='13535371', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3345801', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3345831', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='172840', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='14015081', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='505106', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='2686483011', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3346201', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='172437', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='172426', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3348501', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='3109899011', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='698234', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('Photo', BrowseNode='14015121', ResponseGroup='ItemAttributes,Images', limit=1000,
                                    AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Cams_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def amazonOffice(self,request):

        # get all books from result set and
        # print author and title

        for data in api.item_search('OfficeProducts', BrowseNode='172574',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = Office_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        for data in api.item_search('OfficeProducts', BrowseNode='1069102', ResponseGroup='ItemAttributes,Images',
                                    limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Office_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        for data in api.item_search('OfficeProducts', BrowseNode='1069242', ResponseGroup='ItemAttributes,Images',
                                    limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] = str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"] = "00"

            try:

                request["SNR_SKU"] = "AZ" + str(data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"] = "00"

            try:

                request["SNR_Description"] = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] = "Please visit site to see description"

            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"] = str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] = "None"

            try:

                request["SNR_ImageURL"] = str(data.LargeImage.URL)

            except:

                try:
                    request["SNR_ImageURL"] = str(data.MediumImage.URL)
                except:
                    try:
                        request["SNR_ImageURL"] = str(data.SmallImage.URL)
                    except:
                        request["SNR_ImageURL"] = None

            try:

                request["SNR_UPC"] = str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price = data.ItemAttributes.ListPrice.FormattedPrice
                price = price[1:]
                request["SNR_Price"] = float(price)

            except:

                try:
                    request["SNR_Price"] = (float(data.ItemAttributes.TradeInValue.Amount) / 100)
                except:
                    request["SNR_Price"] = str(0)

            request["SNR_Available"] = "Amazon"

            serializer = Office_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"

                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def amazonVideoGames(self,request):

        # get all books from result set and
        # print author and title
###PC Games
        print "amad"
        for data in api.item_search('VideoGames', BrowseNode='229575',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = 0


            request["SNR_Available"] = "Amazon"





            serializer = VideoGames_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('VideoGames', BrowseNode='14210751',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = VideoGames_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('VideoGames', BrowseNode='6427814011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = VideoGames_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)


        for data in api.item_search('VideoGames', BrowseNode='14220161',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = VideoGames_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



        for data in api.item_search('VideoGames', BrowseNode='6469269011',ResponseGroup='ItemAttributes,Images', limit=1000, AssociateTag='bpl001-20'):
            time.sleep(3)

            # print(objectify.dump(data))
            request["SNR_ProductURL"] =str(data.ItemLinks.ItemLink.URL)
            try:
                request["SNR_Title"] = str(data.ItemAttributes.Title)
            except:
                request["SNR_Title"] = "No Title"

            try:

                request["SNR_ModelNo"] = str(data.ItemAttributes.Model)

            except:
                request["SNR_ModelNo"]="00"



            try:

                request["SNR_SKU"] ="AZ" + str( data.ItemAttributes.EAN)

            except:
                request["SNR_SKU"]="00"



            try:

                request["SNR_Description"]  = str(data.ItemAttributes.Feature)

            except:
                request["SNR_Description"] ="Please visit site to see description"




            try:
                request["SNR_Brand"] = str(data.ItemAttributes.Brand)

            except:

                try:
                    request["SNR_Brand"]= str(data.ItemAttributes.Manufacturer)
                except:
                    request["SNR_Brand"] ="None"



            try:

                request["SNR_ImageURL"]=str(data.LargeImage.URL)

            except :


                try:
                    request["SNR_ImageURL"]= str(data.MediumImage.URL)
                except:
                        try:
                            request["SNR_ImageURL"]=str(data.SmallImage.URL)
                        except:
                            request["SNR_ImageURL"]=None

            try:

                request["SNR_UPC"] =str(data.ItemAttributes.UPC)

            except:
                request["SNR_UPC"] = "000"

            try:

                price=data.ItemAttributes.ListPrice.FormattedPrice
                price=price[1:]
                request["SNR_Price"] =float(price)

            except :

                try:
                    request["SNR_Price"] =(float(data.ItemAttributes.TradeInValue.Amount)/100)
                except:
                    request["SNR_Price"] = str(0)


            request["SNR_Available"] = "Amazon"





            serializer = VideoGames_Serializer(data=request)
            print "done"
            # print serializer


            if serializer.is_valid():
                print "------------------------"


                serializer.save()
            else:
                print "bad jason"
                print serializer.errors
                print serializer.error_messages

                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




