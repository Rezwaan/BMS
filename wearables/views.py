from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .models import Wearable_DB
from .serializers import Wearable_Serializer
from . import ebay
from . import walmart
from . import best
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import groupon
import amazon
# Create your views here.


@api_view(['GET'])
def filterWearables(request,query):
    try:
        que = Q(SNR_Title__icontains=query) | Q(SNR_Description__icontains=query) | Q(SNR_ModelNo__icontains=query) | Q(
            SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que)
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass



@api_view(['GET'])
def filterWearablesDESC(request,query):
    try:
        que = Q(SNR_Title__icontains=query) | Q(SNR_Description__icontains=query) | Q(SNR_ModelNo__icontains=query) | Q(
            SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('-SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass


@api_view(['GET'])
def filterWearablesASC(request,query):
    try:
        que = Q(SNR_Title__icontains=query) | Q(SNR_Description__icontains=query) | Q(SNR_ModelNo__icontains=query) | Q(
            SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)

        wearabledata_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    pass


@api_view(['GET'])
def getAllWearablesModels(request):
    try:
        wearabledata_all = Wearable_DB.objects.exclude(SNR_Available__icontains="Ebay")

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Wearable_Serializer(wearabledata_all,
                                         many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getAll_Wearables(request):
    try:
        wearabledata_all = Wearable_DB.objects.all()
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

@api_view(['GET'])
def getAll_WearablesDESC(request):
    try:
        wearabledata_all = Wearable_DB.objects.all().order_by('-SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

@api_view(['GET'])
def getAll_WearablesASC(request):
    try:
        wearabledata_all = Wearable_DB.objects.all().order_by('SNR_Price')
        paginator = Paginator(wearabledata_all, 12)
        page = request.GET.get('page')
        try:

            users = paginator.page(page)
        except PageNotAnInteger:

            users = paginator.page(1)
        except EmptyPage:

            users = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Wearable_Serializer(users, many=True, context=serializer_context)
        # res = serializer.data
        # res.update('pages_count:', paginator.num_pages())
        # return Response(res)
        items = 0
        pages = 0
        items = paginator._count
        pages = paginator._get_num_pages()
        res = {
            'totalItems': items,
            'totalPages': pages,
            'results': serializer.data

        }
        return Response(res)

    except Wearable_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #
    # if request.method == 'GET':
    #     serializer = Wearable_Serializer(wearabledata_all, many=True)  # many=True so it doesn't return only 1 JSON Object
    #     return Response(serializer.data)
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@ensure_csrf_cookie
@api_view(['POST'])
def add_Wearables(request):

    if request.method == 'POST':

        serializer = Wearable_Serializer(data=request.data)
        #print(serializer)


        if serializer.is_valid():
            print("inserilier")

            #serializer.save()
            requestdata = serializer.validated_data

            #query=mydata["SNR_Name"]+' '+mydata["SNR_Model"]+' '+mydata["SNR_RAM"]
            #

            # amz=amazon.AmazonAPI()
            # amz.amazonWatches(requestdata)

            # group=groupon.GroupOnAPI()
            # group.groupWearable(requestdata)
            # # walmart.wearable_Walmart()
            # bestapi=best.BestbuyAPI()
            # bestapi.Wearables(requestdata)
            ebayapi = ebay.EbayAPI()
            ebayapi.ebayWearables(requestdata)

            # bestapi.search(requestdata)
            # walmart.wearable_Walmart()
            # wallapi=wallmart.WallmartAPI()
            # wallapi.search(requestdata)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


