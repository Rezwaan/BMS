from .serializers import TV_Serializer,Cams_Serializer,CarsElec_Serializer,VideoGames_Serializer,Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,Software_Serializer,Applinces_Serializer,Movies_Serializer,Office_Serializer
import requests
import json
from rest_framework.response import Response    # to send specific response
from rest_framework import status
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()


from models import Cams,OfficeSupply,TV,VideoGames,Applinces,Audio,ComputerSoftware
from wapy.api import Wapy
from serializers import Cams_Serializer
import math
from collections import defaultdict
import time,threading





baseAddress = "http://localhost:8000/"


obj1 = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')







class Offce:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Offce)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def Office_Walmart(categoryId="1229749_1046059_9607197",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = Offce("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=Offce("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=OfficeSupply()
            try:
                obj2 = OfficeSupply.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except OfficeSupply.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Office_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()



class Cam:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Cam):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Cam)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def Cams_Walmart(categoryId="3944_133277_4468",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = Cam("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=Cam("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=Cams()
            try:
                obj2 = Cams.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except Cams.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        Cams_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()



class software:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,software)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def software_Walmart(categoryId="2636",nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = software("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=software("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=ComputerSoftware()
            try:
                obj2 = ComputerSoftware.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except ComputerSoftware.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        software_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()




class WalmartTV:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,WalmartTV)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def TV_Walmart(categoryId="3944_1060825_447913",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = WalmartTV("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=WalmartTV("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=TV()
            try:
                obj2 = TV.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except TV.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        TV_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()





class appliances:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,appliances)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def appliances_Walmart(categoryId="2636",nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = appliances("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=appliances("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=Applinces()
            try:
                obj2 = Applinces.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except Applinces.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        appliances_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()



class audio:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,audio)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def audio_Walmart(categoryId="2636",nextpage=0):
    products,nextpage = obj1.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = audio("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=audio("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=Audio()
            try:
                obj2 = Audio.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except Audio.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        audio_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()







class games:

    def __init__(self,sku,title,model,brand,upc,price,url,imgUrl,desc):
        self.sku = sku
        self.title = title
        self.model = model
        self.brand = brand
        self.upc = upc
        self.price = price
        self.available="Walmart"
        self.productUrl = url
        self.imageUrl = imgUrl
        self.description = desc


    class __metaclass__(type):
        def __iter__(self):
            for attr in dir(Offce):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,games)

#or "Electronics/Computers/Laptop Computers" in product.category_path

def games_Walmart(categoryId="2636",nextpage=0):
    products,nextpage = obj.pagination(categoryId=categoryId,nextpage=nextpage)
    print products
    if len(products)>0:
        for product in products:
            if product.brand_name != None:
                brand=product.brand_name
            if product.available_online == None:
                product.available_online=False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if (product.available_online == True) and (product.sale_price != None):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=games("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=VideoGames()
            try:
                obj2 = VideoGames.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description
            except VideoGames.DoesNotExist:
                obj2.SNR_SKU = laptops[laptop].sku
                obj2.SNR_Title = laptops[laptop].title
                obj2.SNR_ModelNo = laptops[laptop].model
                obj2.SNR_Brand = laptops[laptop].brand
                obj2.SNR_UPC = laptops[laptop].upc
                obj2.SNR_Price = laptops[laptop].price
                obj2.SNR_Available = laptops[laptop].available
                obj2.SNR_ProductURL = laptops[laptop].productUrl
                obj2.SNR_ImageURL = laptops[laptop].imageUrl
                obj2.SNR_Description = laptops[laptop].description

            obj2.save()

    print len(laptops)

    if nextpage!=None:

        time.sleep(0.15)
        games_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()




class WalmartAPI():

    def walmartToys(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=4171&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Toys_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Toys_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None







    def walmartApplinces(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=4044&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Applinces_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Applinces_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None







    def walmartMovies(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=4096&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Movies_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Movies_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartSmartHome(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=1229875&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Smarthomes_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Smarthomes_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartCarsElec(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=3944_538883&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = CarsElec_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = CarsElec_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartVideoGame(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=2636&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = VideoGames_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = VideoGames_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartCamera(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=3944_133277_1096663&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Cams_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Cams_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartAudio(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=3944_96469_164001&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Audio_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Audio_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartSoftware(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=3944_3951_443023&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Software_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        print (data['nextPage'])

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            print ("H_-------------------------------------------------------------------")
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Software_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartOffice(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=1229749&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Office_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            print "_________________________________________________________________"
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = Office_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None




    def walmartTV1(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=3944_1060825_447913&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = TV_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            print "_________________________________________________________________"
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = TV_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None


    def walmartTV2(self,request):

        response = requests.get(
            "http://api.walmartlabs.com/v1/paginated/items?category=3944_77622&specialOffer=rollback&apiKey=m9esvpqxg8vc85g97726vdmn&format=json&sort=price&order=asc")
        data = json.loads(response.text)
        # print(data)
        for item in data['items']:

            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = TV_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'nextPage' in data:

            nextcall = data['nextPage']
        else:
            print "_________________________________________________________________"
            nextcall = None

        print "Next Call" + nextcall
        while (nextcall != None):
            response = requests.get(
                "http://api.walmartlabs.com" + nextcall + "&sort=price&order=asc")
            data = json.loads(response.text)
            request["SNR_Available"] = "Walmart"

            request["SNR_SKU"] = "Wl" + str(item['itemId'])

            if 'shortDescription' in item:
                request["SNR_Description"] = item['shortDescription']
            else:
                request["SNR_Description"] = "Not Available"


            if 'brandName' in item:
                request["SNR_Brand"] = item['brandName']
            else:
                request["SNR_Brand"] = "Not Available"

            if 'largeImage' in item:
                request["SNR_ImageURL"] = item['largeImage']
            else:
                request["SNR_ImageURL"]="0000"

            if 'productTrackingUrl' in item:
                request["SNR_ProductURL"] = item['productTrackingUrl']
            else:
                request["SNR_ProductURL"] ="00"

            if 'salePrice' in item:
                request["SNR_Price"] = item['salePrice']
            else:
                request["SNR_Price"] = "0000"

            if 'modelNumber' in item:
                request["SNR_ModelNo"] = item['modelNumber']
            else:
                request["SNR_ModelNo"] = "Not Available"

            request["SNR_Title"] = item['name']

            if 'upc' not in item:
                request["SNR_UPC"] = "000000"
            else:
                request["SNR_UPC"] = item['upc']

            serializer = TV_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print "------"
                serializer.save()
            else:
                print("bad json")
                # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



            if 'nextPage' in data:

                nextcall = data['nextPage']
            else:
                nextcall = None

