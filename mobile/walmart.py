import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()


from collections import defaultdict
import time,threading
from mobile.models import Mobile_DB



from django.conf import settings



from wapy.api import Wapy

from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from mobile.serializer import Mobile_Serializer

# obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')


class Mobile:

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
            for attr in dir(Mobile):
                if not attr.startswith("__"):
                    yield attr




mobiles=defaultdict(lambda: None,Mobile)
mobileBrands=["samsung","apple","microsoft","nokia","sony","htc","motorola","lg","huawei",
              "lenovo","xiaomi","google","acer","asus","oppo","oneplus","meizu",
              "blackberry","alcatel","zte","toshiba","vodafone","gigabyte","xolo",
              "lava","micromax","blu","gionee","vivo","leeco","panasonic","hp",
              "yu","verykool","maxwest","plum"]

#Cell Phones/Unlocked Phones
def mobile_Walmart(categoryId="3944_542371_1073085",nextpage=0):

    products, nextpage = obj.pagination(categoryId=categoryId, nextpage=nextpage)
    #print products
    if len(products) > 0:
        for product in products:
            if product.brand_name != None:
                brand = product.brand_name
            if product.available_online == None:
                product.available_online = False

            if product.large_image != None:
                image = product.large_image
            elif product.medium_image != None:
                image = product.medium_image
            else:
                image = product.thumbnail_image

            if ("Cell Phones/Unlocked Phones" not in product.category_path) and (
                "Accessories" not in product.category_path) and (product.available_online == True) and (
                product.sale_price != None) and (brand.lower() in mobileBrands):
                print product.available_online
                if product.model_number != None and mobiles[product.model_number] == None:
                    mobiles[product.model_number] = Mobile("WM" + str(product.item_id), product.name,
                                                           product.model_number, product.brand_name, product.upc,
                                                           product.sale_price, product.product_url,
                                                           image, product.long_description)
                elif product.model_number != None and mobiles[product.model_number] != None:
                    if mobiles[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        mobiles[product.model_number] = Mobile("WM" + str(product.item_id), product.name,
                                                               product.model_number, product.brand_name, product.upc,
                                                               product.sale_price, product.product_url,
                                                               image, product.long_description)
                        print mobiles[product.model_number], mobiles[product.model_number].title, mobiles[
                            product.model_number].price, mobiles[product.model_number].productUrl

                        # for laptop in laptops:
                        # print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # print "end"
        nextpage = None


        for model in mobiles:

            obj2 = Mobile_DB()
            try:
                obj2 = Mobile_DB.objects.get(SNR_SKU=mobiles[model].sku, SNR_ProductURL=mobiles[model].productUrl)
                obj2.SNR_SKU = mobiles[model].sku
                obj2.SNR_Title = mobiles[model].title
                obj2.SNR_ModelNo = mobiles[model].model
                obj2.SNR_Brand = mobiles[model].brand
                obj2.SNR_UPC = mobiles[model].upc
                obj2.SNR_Price = mobiles[model].price
                obj2.SNR_Available = mobiles[model].available
                obj2.SNR_ProductURL = mobiles[model].productUrl
                obj2.SNR_ImageURL = mobiles[model].imageUrl
                obj2.SNR_Description = mobiles[model].description
            except Mobile_DB.DoesNotExist:
                obj2.SNR_SKU = mobiles[model].sku
                obj2.SNR_Title = mobiles[model].title
                obj2.SNR_ModelNo = mobiles[model].model
                obj2.SNR_Brand = mobiles[model].brand
                obj2.SNR_UPC = mobiles[model].upc
                obj2.SNR_Price = mobiles[model].price
                obj2.SNR_Available = mobiles[model].available
                obj2.SNR_ProductURL = mobiles[model].productUrl
                obj2.SNR_ImageURL = mobiles[model].imageUrl
                obj2.SNR_Description = mobiles[model].description

            obj2.save()

    print len(mobiles)

    if nextpage != None:
        #for model in mobiles:
            #print mobiles[model].model, mobiles[model].title, mobiles[model].price, mobiles[model].productUrl
        time.sleep(0.15)
        mobile_Walmart(categoryId, nextpage)





class WallmartAPI():




    def search(self,request):
        print("hello")

        obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')


        query=request["SNR_Name"]+' '+request["SNR_Model"]


        products = obj.search(query=query, sort='price', order='asc',facet='on',facetfilter='category:Cell Phones',numItems=25)
        price="";
        url="";
        name="";
        if len(products) > 0:
                for product in products:
                    if "Cell Phones" in product.category_path and "Accessories" not in product.category_path and "NO PHONE" not in product.name :

                        # print product.name
                        # print product.sale_price
                        # print product.product_url
                        # print product.category_path
                        # print product.category_node
                        # print product.available_online
                        name=product.name
                        price=product.sale_price
                        url=product.product_url

        else:

                print "no products found"


        request["SNR_Price"]=price
        request["SNR_Link"]=url
        request["SNR_CompleteName"]=name
        request["SNR_Available"]="WALLMART"

        #
        # print(price)
        # print (url)
        # print ("before add")
        serializer = Mobile_Serializer(data=request)
        if serializer.is_valid():

            serializer.save()

        else:
            print ("json not good")
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)




if __name__ == '__main__':
    mobile_Walmart()