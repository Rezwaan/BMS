__author__ = 'Amad'
import requests
from bs4 import BeautifulSoup
from .serializer import Mobile_Serializer
import unicodedata

class ATNT():
    def getAllMobile(self,request):
        url='https://www.att.com/shop/wireless/devices/cellphones.html'
        source=requests.get(url)
        plain_text=source.text
        soup= BeautifulSoup(plain_text,"lxml")
        titles=[]
        images=[]
        prooductlinks=[]
        prices=[]
        sku=[]
        descriptons=[]
        ratinglink=[]

        for link in soup.findAll('a',{'class':'titleURLchng'}):


            lin="https://www.att.com"+link.get('href')
            prooductlinks.append(lin)
            title= link.string
            SKU=link.get('data-cskuid')
            sku.append(SKU)

            titles.append(title)

        for link in soup.findAll('img',{'class':'inStockOpacity'}  ):

            img=link.get('src')

            images.append(img)

        for link in soup.findAll('div',{'class':'list-description'}  ):

            des=link.get_text()
            descriptons.append(des)

        count=0
        for l in soup.findAll('div',{'class':'list-price'}):

            price=l.get_text()
            prices.append(price)
        for link in soup.findAll('a',{'class':'clickStreamSingleItem rtngURLchng'}):


            lin="https://www.att.com"+link.get('href')
            ratinglink.append(lin)


        count=0;
        for var in descriptons:


            desc=unicodedata.normalize('NFKD', var).encode('ascii','ignore')
            desc=desc.strip()
            title=unicodedata.normalize('NFKD', titles[count]).encode('ascii','ignore')
          #  skuu=unicodedata.normalize('NFKD', sku[count]).encode('ascii','ignore')
            prc=unicodedata.normalize('NFKD', prices[count]).encode('ascii','ignore')

            #print(desc)

            title=title.strip()
            prc=prc.strip()
            #print(title)




            # print titles[count]
            #
            # print(titles[count]+"   "+str(sku[count]))
            # cell = unicode(descriptons[count]).replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
            #
            #
            # print(str(cell))
            prc=prc.strip()
            print(prc)
            # print(images[count])
            request["SNR_Price"]=prc
            request["SNR_Brand"]="00"
            request["SNR_Available"]="AT&T"
            request["SNR_Description"]=desc
            request["SNR_Title"]=title
            request["SNR_ImageURL"]=images[count]
            request["SNR_ProductURL"]=prooductlinks[count]
            request["SNR_ModelNo"]=title
            request["SNR_SKU"]="AT"+str(sku[count])
            request["SNR_UPC"]="00"
            # request["SNR_ReviewLink"]=requests[count]

            serializer = Mobile_Serializer(data=request)
            print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print("---")
                serializer.save()
            else:
                print("bad json")


            count=count+1