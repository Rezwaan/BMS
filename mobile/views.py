from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from . models import Mobile_DB
from . serializer import Mobile_Serializer
import best
from django.views.decorators.csrf import ensure_csrf_cookie
import ebay
import ATnT
import walmart
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import groupon
import amazon
import newegg
def index(request):
    return HttpResponse("<h1>Something NOT WELL</h1>")




#######################Filter Mobiles
@api_view(['GET'])
def Filter_Mobiles(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass



#######################Filter Mobiles
@api_view(['GET'])
def Filter_MobilesDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass



#######################Filter Mobiles
@api_view(['GET'])
def Filter_MobilesASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          users = paginator.page(page)
       except PageNotAnInteger:

           users = paginator.page(1)
       except EmptyPage:

           users = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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


   except Mobile_DB.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


   # if request.method == 'GET':
   #
   #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
   #     return Response(serializer.data)
   # else:
   #
   #     return Response(status=status.HTTP_400_BAD_REQUEST)
   #
   pass


#######################View all mobiles
@api_view(['GET'])
def getAll_Mobiles(request):
    try:

        Mobile_all = Mobile_DB.objects.all()
        paginator = Paginator(Mobile_all, 12)

        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
            users = paginator.page(paginator.num_pages)
        serializer_context = {'request': request}
        serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def getAll_MobilesASC(request):
    try:

        Mobile_all = Mobile_DB.objects.all().order_by('SNR_Price')
        paginator = Paginator(Mobile_all, 12)

        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
            users = paginator.page(paginator.num_pages)
        serializer_context = {'request': request}
        serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getAll_MobilesDESC(request):
    try:

        Mobile_all = Mobile_DB.objects.all().order_by('-SNR_Price')
        paginator = Paginator(Mobile_all, 12)

        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999),
        # deliver last page of results.
            users = paginator.page(paginator.num_pages)
        serializer_context = {'request': request}
        serializer = Mobile_Serializer(users,many=True,context=serializer_context)
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

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


#######################View all mobiles
@api_view(['GET'])
def getModels(request):
    try:


        Mobile_all = Mobile_DB.objects.filter(SNR_Available__icontains="Best Buy")

    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

######### Adding new Mobiles

@ensure_csrf_cookie
@api_view(['POST'])
def add_Mobiles(request):

    if request.method == 'POST':

        serializer = Mobile_Serializer(data=request.data)
        #print(serializer)


        if serializer.is_valid():
            print("inserilier")

            #serializer.save()
            requestdata = serializer.validated_data

            neww=newegg.newEggAPI()
            neww.newEggMobiles(requestdata)

            # group= groupon.GroupOnAPI()
            # group.groupPhones(requestdata)

            # amz= amazon.AmazonAPI()
            # amz.amazonMobile(requestdata)


            # bestapi = best.bestAPI()
            # bestapi.getMobile(requestdata)

            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayMobiles(requestdata)
            #
            # walmart.mobile_Walmart()
            #
            # #bestapi.search(requestdata)
            # atnt= ATnT.ATNT()
            # atnt.getAllMobile(requestdata)

            # wallapi=wallmart.WallmartAPI()
            # wallapi.search(requestdata)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

