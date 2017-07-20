
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()


from wapy.api import Wapy
from wearables.serializers import Wearable_Serializer
import time
from collections import defaultdict
from wearables.models import Wearable_DB


# obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')


class Wearable:

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
            for attr in dir(Wearable):
                if not attr.startswith("__"):
                    yield attr





wearables=defaultdict(lambda: None,Wearable)
Accessories=["tempered glass","screen protector","protective case",
                 "protective holder","silicone replacement","wrist band",
                 "bracelet strap","watch case","band strap",
                 "sports band","sports bracelet","replacement silicone",
                 "sports strap","watch band","dock charger","watch charging",
                 "wireless charger","dock station","wrist strap","wrap",
                 "skin decal","replacement","accessory","accessory band",
                 "replace","loop band","woven nylon","sport nylon","nylon band",
                 "leather loop","stand","ipm","sport bands","cable","battery","band"]


accessoryFound = False
appleAccessoryFound = False
#Wearable
def wearable_Walmart(nextpage=0,appleNextpage=0):
    products, nextpage = obj.pagination(categoryId="3944_1229723", nextpage=nextpage)
    appleProducts, appleNextpage = obj.pagination(categoryId="3944_1086506_1089150", nextpage=appleNextpage)
    #print products
    if len(products) > 0 or len(appleProducts) > 0:

        if len(products) > 0:
            for product in products:

                if product.available_online == None:
                    product.available_online = False

                if product.large_image != None:
                    image = product.large_image
                elif product.medium_image != None:
                    image = product.medium_image
                else:
                    image = product.thumbnail_image

                for accessory in Accessories:
                    if accessory in product.name.lower() and accessoryFound == False:
                        print "accessory found"
                        accessoryFound = True
                    else:
                        accessoryFound = False

                if (accessoryFound == False) and (product.available_online == True) and (product.sale_price != None):
                    print "enter"
                    #print product.available_online
                    if product.model_number != None and wearables[product.model_number] == None:
                        wearables[product.model_number] = Wearable("WM" + str(product.item_id), product.name,
                                                               product.model_number, product.brand_name, product.upc,
                                                               product.sale_price, product.product_url,
                                                               image, product.long_description)
                    elif product.model_number != None and wearables[product.model_number] != None:
                        if wearables[product.model_number].price > product.sale_price:
                            #print("same model found with lower price")
                            wearables[product.model_number] = Wearable("WM" + str(product.item_id), product.name,
                                                                   product.model_number, product.brand_name, product.upc,
                                                                   product.sale_price, product.product_url,
                                                                   image, product.long_description)
                            #print wearables[product.model_number].model, wearables[product.model_number].title, wearables[product.model_number].price, wearables[product.model_number].productUrl

                            # for laptop in laptops:
                            # print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl

        if len(appleProducts) > 0:
            for product in appleProducts:

                if product.available_online == None:
                    product.available_online = False

                if product.large_image != None:
                    image = product.large_image
                elif product.medium_image != None:
                    image = product.medium_image
                else:
                    image = product.thumbnail_image

                for accessory in Accessories:
                    if accessory in product.name.lower() and appleAccessoryFound == False:
                        #print "accessory found"
                        appleAccessoryFound = True
                    else:
                        appleAccessoryFound = False

                if (appleAccessoryFound == False) and (product.available_online == True) and (product.sale_price != None) and "apple" in product.name.lower():
                    print "enter"
                    #print product.available_online
                    if product.model_number != None and wearables[product.model_number] == None:
                        wearables[product.model_number] = Wearable("WM" + str(product.item_id), product.name,
                                                                   product.model_number, product.brand_name,
                                                                   product.upc,
                                                                   product.sale_price, product.product_url,
                                                                   image, product.long_description)
                    elif product.model_number != None and wearables[product.model_number] != None:
                        if wearables[product.model_number].price > product.sale_price:
                     #       print("same model found with lower price")
                            wearables[product.model_number] = Wearable("WM" + str(product.item_id), product.name,
                                                                       product.model_number, product.brand_name,
                                                                       product.upc,
                                                                       product.sale_price, product.product_url,
                                                                       image,
                                                                       product.long_description)
                      #      print wearables[product.model_number].model, wearables[product.model_number].title,wearables[product.model_number].price, wearables[product.model_number].productUrl

                            # for laptop in laptops:
                            # print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        # print "end"
        nextpage = None
        appleNextpage = None


        for model in wearables:

            obj2 = Wearable_DB()
            try:
                obj2 = Wearable_DB.objects.get(SNR_SKU=wearables[model].sku, SNR_ProductURL=wearables[model].productUrl)
                obj2.SNR_SKU = wearables[model].sku
                obj2.SNR_Title = wearables[model].title
                obj2.SNR_ModelNo = wearables[model].model
                obj2.SNR_Brand = wearables[model].brand
                obj2.SNR_UPC = wearables[model].upc
                obj2.SNR_Price = wearables[model].price
                obj2.SNR_Available = wearables[model].available
                obj2.SNR_ProductURL = wearables[model].productUrl
                obj2.SNR_ImageURL = wearables[model].imageUrl
                obj2.SNR_Description = wearables[model].description
            except Wearable_DB.DoesNotExist:
                obj2.SNR_SKU = wearables[model].sku
                obj2.SNR_Title = wearables[model].title
                obj2.SNR_ModelNo = wearables[model].model
                obj2.SNR_Brand = wearables[model].brand
                obj2.SNR_UPC = wearables[model].upc
                obj2.SNR_Price = wearables[model].price
                obj2.SNR_Available = wearables[model].available
                obj2.SNR_ProductURL = wearables[model].productUrl
                obj2.SNR_ImageURL = wearables[model].imageUrl
                obj2.SNR_Description = wearables[model].description

            obj2.save()


    print len(wearables)

    if nextpage != None or appleNextpage != None:
        # for model in wearables:
        #     print wearables[model].model, wearables[model].title, wearables[model].price, wearables[model].productUrl

        time.sleep(0.30)
        wearable_Walmart(nextpage,appleNextpage)





def search(data):
    print "Walmant Api Called"

    query = data["title_SNR"] + ' ' + data["model_SNR"]

    #http://api.walmartlabs.com/v1/search?query=apple watch series&format=json&sort=price&order=asc&categoryId=3944_1229723&apiKey=2rqq8n6afjjdwtsp7xacr7gb&numItems=25

    Accessories=["tempered glass","screen protector","protective case",
                 "protective holder","silicone replacement","wrist band",
                 "bracelet strap","watch case","band strap",
                 "sports band","sports bracelet","replacement silicone",
                 "sports strap","watch band","dock charger","watch charging",
                 "wireless charger","dock station","wrist strap","wrap",
                 "skin decal","replacement","accessory","accessory band",
                 "replace","loop band","woven nylon","sport nylon","nylon band",
                 "leather loop","stand","ipm","sport bands"]



    #http://api.walmartlabs.com/v1/search?query=apple watch&format=json&sort=price&order=asc
    #&categoryId=3944_1086506_1089150&apiKey=2rqq8n6afjjdwtsp7xacr7gb&numItems=25&start=25
    page = 1
    productFound = False

    if "apple" in data["title_SNR"].lower():

        while productFound==False:
            products = obj.search(query=query , sort='price', order='asc', numItems=25, categoryId="3944_1086506_1089150",page=page)

            if len(products) > 0:
                #print products
                for product in products:
                    #print product.item_id
                    print product.name
                    print product.sale_price
                    #print product.product_url
                    #print product.category_path
                    #print product.category_node
                    print product.available_online
                    accessoryFound=False
                    for accessory in Accessories:
                        if accessory in product.name.lower() and accessoryFound==False and product.sale_price<150.00:
                            accessoryFound=True

                    if accessoryFound==False:
                        if query.lower() in product.name.lower() and product.available_online == True:
                            print product.name
                            print product.sale_price
                            productFound=True
                            if "refurbished" in product.name.lower():
                                data["condition_SNR"] = "Refurbished"
                            data["link_SNR"] = product.product_url
                            data["price_SNR"] = product.sale_price
                            serializer = Wearable_Serializer(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                break

                if len(products)<25:
                    break
                else:
                    page = page + 1


            else:
                print "Walmart Product not found"
                break


    else:

        while productFound == False:
            products = obj.search(query=query, sort='price', order='asc', numItems=25,categoryId="3944_1229723", page=page)
            if len(products) > 0:
                #print products

                for product in products:
                    # print product.item_id
                    #print product.name
                    print product.sale_price
                    # print product.product_url
                    # print product.category_path
                    # print product.category_node
                    print product.available_online
                    accessoryFound = False
                    for accessory in Accessories:
                        if accessory in product.name.lower() and accessoryFound == False and product.sale_price < 20.00:
                            accessoryFound = True

                    if accessoryFound == False:
                        if query.lower() in product.name.lower() and product.available_online == True:
                            print product.name
                            print product.sale_price

                            productFound = True

                            if "refurbished" in product.name.lower():
                                data["condition_SNR"] = "Refurbished"
                            data["link_SNR"] = product.product_url
                            data["price_SNR"] = product.sale_price

                            serializer = Wearable_Serializer(data=data)
                            if serializer.is_valid():
                                serializer.save()
                                break

                if len(products)<25:
                    break
                else:
                    page = page + 1


            else:
                print "Walmart Product not found"
                break



if __name__ == '__main__':
    wearable_Walmart()