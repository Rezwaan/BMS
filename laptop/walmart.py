import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()


from models import Laptop_DB
from wapy.api import Wapy
from serializers import Laptop_Serializer
import math
from collections import defaultdict
import time,threading





from django.conf import settings





# obj = Wapy('2rqq8n6afjjdwtsp7xacr7gb')
obj = Wapy('m9esvpqxg8vc85g97726vdmn')
class Laptop:

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
            for attr in dir(Laptop):
                if not attr.startswith("__"):
                    yield attr






laptops=defaultdict(lambda: None,Laptop)
laptopBrands=["apple","hp","dell","asus","acer","lenovo","samsung"]

#or "Electronics/Computers/Laptop Computers" in product.category_path

def laptop_Walmart(categoryId="3944_3951_132960",nextpage=0):
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

            if ("Type/All Laptop Computers" in product.category_path) and ("Accessories" not in product.category_path) and (product.available_online == True) and (product.sale_price != None) and (brand.lower() in laptopBrands):
                print product.available_online
                if product.model_number != None and laptops[product.model_number] == None:
                    laptops[product.model_number] = Laptop("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                elif product.model_number != None and laptops[product.model_number] != None:
                    if laptops[product.model_number].price > product.sale_price:
                        print("same model found with lower price")
                        laptops[product.model_number]=Laptop("WM"+str(product.item_id),product.name,product.model_number,product.brand_name,product.upc,product.sale_price,product.product_url,image,product.long_description)
                        print laptops[product.model_number], laptops[product.model_number].title, laptops[product.model_number].price , laptops[product.model_number].productUrl

        #for laptop in laptops:
            #print laptop, laptops[laptop].title, laptops[laptop].price , laptops[laptop].productUrl
    else:
        #print "end"
        nextpage=None

        for laptop in laptops:

            obj2=Laptop_DB()
            try:
                obj2 = Laptop_DB.objects.get(SNR_SKU=laptops[laptop].sku, SNR_ProductURL=laptops[laptop].productUrl)
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
            except Laptop_DB.DoesNotExist:
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
        laptop_Walmart(categoryId,nextpage)
        #threading.Timer(0.15,test2(categoryId,nextpage)).start()







'''
def search(data):

    print "Walmant Api Called"

    query = data["SNR_Title"] + ' ' + data["SNR_Brand"] + ' ' + data["SNR_ModelNo"]

    if data["SNR_Brand"].lower() == "lenovo" and "g" in data["SNR_ModelNo"].lower() :
        products = obj.search(query=query, sort='price', order='asc', facet='on',facetfilter='category:laptop',numItems=25)

        if len(products) > 0:
            #print products
            for product in products:
                # print product.item_id
                #print product.name
                # print product.sale_price
                # print product.product_url
                # print product.category_path
                # print product.category_node
                # print product.available_online
                if query.lower() in product.name.lower() and product.available_online == True:
                    print product.name
                    if "refurbished" in product.name.lower():
                        data["condition_SNR"] = "Refurbished"
                    data["link_SNR"] = product.product_url
                    data["price_SNR"] = product.sale_price
                    serializer = Laptop_Serializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        break

        else:
            print "Walmart Product not found"

    else:
        products = obj.search(query=query+"&facet.filter=category:laptop", sort='price', order='asc', facet='on',numItems=25)

        if len(products) > 0:
            #print products
            for product in products:
                #print product.item_id
                #print product.name
                #print product.sale_price
                #print product.product_url
                #print product.category_path
                #print product.category_node
                #print product.available_online
                if query.lower() in product.name.lower() and product.available_online == True:
                    print product.name
                    if "refurbished" in product.name.lower():
                        data["condition_SNR"] = "Refurbished"
                    data["link_SNR"] = product.product_url
                    data["price_SNR"] = product.sale_price
                    serializer = Laptop_Serializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        break

        else:
            print "Walmart Product not found"

'''

if __name__ == '__main__':
    laptop_Walmart()
