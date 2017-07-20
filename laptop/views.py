
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .models import Laptop_DB
from .serializers import Laptop_Serializer
import walmart
import ebay
import best
import ATnT
import amazon
import newegg
# Create your views here.
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import groupon

@api_view(['DELETE'])
def delete(self):

    snippet = Laptop_DB.objects.all()
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def FilterLaptops(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que)
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass





@api_view(['GET'])
def FilterLaptopsAsc(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass




@api_view(['GET'])
def FilterLaptopsDesc(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Laptop_all, 12)
       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0
       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)

   #
   # if request.method == 'GET':
   #
   #     serializer = Laptop_Serializer(Laptop_all, many=True) # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)

   pass




@api_view(['GET'])
def getAllLaptopsSortASC(request):
    try:

        laptopdata_all = Laptop_DB.objects.all().order_by('SNR_Price')
        paginator = Paginator(laptopdata_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator._count
        pages=paginator.num_pages
        res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

         }
        return Response(res)

    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Laptop_Serializer(laptopdata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass


@api_view(['GET'])
def getAllLaptopsSortDESC(request):
    try:

        laptopdata_all = Laptop_DB.objects.all().order_by('-SNR_Price')
        paginator = Paginator(laptopdata_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator._count
        pages=paginator.num_pages
        res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

         }
        return Response(res)

    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Laptop_Serializer(laptopdata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass






@api_view(['GET'])
def getAll_Laptops(request):
    try:

        laptopdata_all = Laptop_DB.objects.all()
        paginator = Paginator(laptopdata_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Laptop_Serializer(data,many=True,context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
        items=0
        pages=0
        items=paginator._count
        pages=paginator.num_pages
        res={
       'totalItems':items,
       'totalPages':pages,
       'results': serializer.data

         }
        return Response(res)

    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Laptop_Serializer(laptopdata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass

@api_view(['POST'])
def add_Laptop(request):

    if request.method == 'POST':

        serializer = Laptop_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            # walmart.laptop_Walmart()


            # amazondata= amazon.AmazonAPI()
            # amazondata.amazonLaptops(mydata)

            newegg.newEggAPI().newEggLaptops(mydata)


            # bestBuy= best.bestbuy()
            # bestBuy.getLaptops(mydata)
            # #
            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayLaptops(mydata)
            #
            # atnt= ATnT.ATNT()
            # atnt.getLaptops(mydata)
            #
            # group= groupon.GroupOnAPI()
            # group.groupLaptop(mydata)



            # walmart.search(mydata)
            #
            # ebay.search(mydata)
            #
            # best.search(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getModels(request):
    try:


        Mobile_all = Laptop_DB.objects.filter(SNR_Available__icontains="Best Buy")
    except Laptop_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Laptop_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass
