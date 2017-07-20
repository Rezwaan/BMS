from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from .models import TV,Cams,CarsElectronics,VideoGames,Toys,SmartHomes,Audio,ComputerSoftware,Applinces,Movies,OfficeSupply,HealthandFitness
from .serializers import TV_Serializer,Cams_Serializer,CarsElec_Serializer,VideoGames_Serializer,\
    Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,Software_Serializer, Applinces_Serializer,Movies_Serializer,Office_Serializer,Health_Serializer
import walmart
import ebay
import best
import groupon
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import amazon

@api_view(['GET'])
def Filter_Appliences(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = Applinces.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Applinces_Serializer(record,many=True,context=serializer_context)
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


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def Filter_Health(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = HealthandFitness.objects.filter(que)
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Health_Serializer(record,many=True,context=serializer_context)
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


   except HealthandFitness.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)






@api_view(['GET'])
def Filter_HealthASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = HealthandFitness.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Health_Serializer(record,many=True,context=serializer_context)
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


   except HealthandFitness.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)







@api_view(['GET'])
def Filter_AppliencesASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = Applinces.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Applinces_Serializer(record,many=True,context=serializer_context)
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


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_AppliencesDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = Applinces.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Applinces_Serializer(record,many=True,context=serializer_context)
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


   except Applinces.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_HealthDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       Mobile_all = HealthandFitness.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(Mobile_all, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Health_Serializer(record,many=True,context=serializer_context)
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


   except HealthandFitness.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_videogames(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = VideoGames.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = VideoGames_Serializer(record,many=True,context=serializer_context)
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


   except VideoGames.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_videogamesASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = VideoGames.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page).order_by('SNR_Price')
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = VideoGames_Serializer(record,many=True,context=serializer_context)
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


   except VideoGames.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_videogamesDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = VideoGames.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = VideoGames_Serializer(record,many=True,context=serializer_context)
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


   except VideoGames.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def Filter_audio(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Audio.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Audio_Serializer(record,many=True,context=serializer_context)
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


   except Audio.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def Filter_audioASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Audio.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Audio_Serializer(record,many=True,context=serializer_context)
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


   except Audio.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def Filter_audioDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Audio.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Audio_Serializer(record,many=True,context=serializer_context)
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


   except Audio.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_cams(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Cams.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Cams_Serializer(record,many=True,context=serializer_context)
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


   except Cams.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_camsASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Cams.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Cams_Serializer(record,many=True,context=serializer_context)
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


   except Cams.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_camsDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Cams.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Cams_Serializer(record,many=True,context=serializer_context)
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


   except Cams.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_smarthome(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = SmartHomes.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Smarthomes_Serializer(record,many=True,context=serializer_context)
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


   except SmartHomes.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_smarthomeASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = SmartHomes.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Smarthomes_Serializer(record,many=True,context=serializer_context)
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


   except SmartHomes.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_smarthomeDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = SmartHomes.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Smarthomes_Serializer(record,many=True,context=serializer_context)
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


   except SmartHomes.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def Filter_carselectronics(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = CarsElectronics.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = CarsElec_Serializer(record,many=True,context=serializer_context)
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


   except CarsElectronics.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_carselectronicsASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = CarsElectronics.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = CarsElec_Serializer(record,many=True,context=serializer_context)
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


   except CarsElectronics.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_carselectronicsDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = CarsElectronics.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = CarsElec_Serializer(record,many=True,context=serializer_context)
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


   except CarsElectronics.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_movies(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Movies.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Movies_Serializer(record,many=True,context=serializer_context)
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


   except Movies.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_moviesASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Movies.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Movies_Serializer(record,many=True,context=serializer_context)
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


   except Movies.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_moviesDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Movies.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Movies_Serializer(record,many=True,context=serializer_context)
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


   except Movies.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def Filter_software(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = ComputerSoftware.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Software_Serializer(record,many=True,context=serializer_context)
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


   except ComputerSoftware.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_softwareASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = ComputerSoftware.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Software_Serializer(record,many=True,context=serializer_context)
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


   except ComputerSoftware.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_softwareDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Software_Serializer(record,many=True,context=serializer_context)
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


   except ComputerSoftware.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)







@api_view(['GET'])
def Filter_office(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = OfficeSupply.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Office_Serializer(record,many=True,context=serializer_context)
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


   except OfficeSupply.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_officeASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = OfficeSupply.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Office_Serializer(record,many=True,context=serializer_context)
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


   except OfficeSupply.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_officeDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = OfficeSupply.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Office_Serializer(record,many=True,context=serializer_context)
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


   except OfficeSupply.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_toys(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Toys.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Toys_Serializer(record,many=True,context=serializer_context)
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


   except Toys.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_toysASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Toys.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Toys_Serializer(record,many=True,context=serializer_context)
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


   except Toys.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def Filter_toysDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = Toys.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = Toys_Serializer(record,many=True,context=serializer_context)
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


   except Toys.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
def Filter_tv(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = TV.objects.filter(que)
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = TV_Serializer(record,many=True,context=serializer_context)
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


   except TV.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_tvASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = TV.objects.filter(que).order_by('SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = TV_Serializer(record,many=True,context=serializer_context)
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


   except TV.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def Filter_tvDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_Description__icontains=query) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)
       data = TV.objects.filter(que).order_by('-SNR_Price')
       paginator = Paginator(data, 12)
       page = request.GET.get('page')
       try:

          record = paginator.page(page)
       except PageNotAnInteger:

           record = paginator.page(1)
       except EmptyPage:

           record = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       serializer = TV_Serializer(record,many=True,context=serializer_context)
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


   except TV.DoesNotExist:

       return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getModelsOffice(request):
    try:


        data = OfficeSupply.objects.exclude(SNR_Available__icontains="Ebay")
    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Office_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsHealth(request):
    try:


        data = HealthandFitness.objects.exclude(SNR_Available__icontains="Ebay")
    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Health_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def getModelsApplinces(request):
    try:


        data = Applinces.objects.filter(SNR_Available__icontains="Best Buy")
    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Applinces_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def getModelsSoftware(request):
    try:


        data = ComputerSoftware.objects.filter(SNR_Available__icontains="Best Buy")
    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Software_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def getModelsSmarthome(request):
    try:


        data = SmartHomes.objects.exclude(SNR_Available__icontains="Ebay")
    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Smarthomes_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsToys(request):
    try:


        data = Toys.objects.exclude(SNR_Available__icontains="Ebay")
    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Toys_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def getModelsTV(request):
    try:


        data = TV.objects.filter(SNR_Available__icontains="Best Buy")
    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = TV_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsCams(request):
    try:


        data = Cams.objects.filter(SNR_Available__icontains="Best Buy")
    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Cams_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass

@api_view(['GET'])
def getModelsCarElec(request):
    try:


        data = CarsElectronics.objects.filter(SNR_Available__icontains="Best Buy")
    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = CarsElec_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass






@api_view(['GET'])
def getModelsAudio(request):
    try:


        data = Audio.objects.filter(SNR_Available__icontains="Best Buy")
    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Applinces_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsMovies(request):
    try:


        data = Movies.objects.filter(SNR_Available__icontains="Best Buy")
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = Movies_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET'])
def getModelsGames(request):
    try:


        data = VideoGames.objects.exclude(SNR_Available__icontains="Ebay")
    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = VideoGames_Serializer(data, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass




@api_view(['GET'])
def getAll_Applinces(request):
    try:

        data_all = Applinces.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(data,many=True,context=serializer_context)
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

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getAll_Health(request):
    try:

        data_all = HealthandFitness.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(data,many=True,context=serializer_context)
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

    except HealthandFitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_OfficeItems(request):
    try:

        data_all = OfficeSupply.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(data,many=True,context=serializer_context)
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

    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_Movies(request):
    try:

        data_all = Movies.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(data,many=True,context=serializer_context)
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

    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_software(request):
    try:

        data_all = ComputerSoftware.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(data,many=True,context=serializer_context)
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

    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_Toys(request):
    try:

        data_all = Toys.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(data,many=True,context=serializer_context)
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

    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAll_Audio(request):
    try:

        data_all = Audio.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(data,many=True,context=serializer_context)
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

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAll_SmartHomes(request):
    try:

        data_all = SmartHomes.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(data,many=True,context=serializer_context)
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

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getAll_CarsElectronics(request):
    try:

        data_all = CarsElectronics.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(data,many=True,context=serializer_context)
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

    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])

def getAll_Cams(request):
    try:

        data_all = Cams.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(data,many=True,context=serializer_context)
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

    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_videoGames(request):
    try:

        data_all = VideoGames.objects.all()
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(data,many=True,context=serializer_context)
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

    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_TV(request):
    try:

        laptopdata_all = TV.objects.all()
        paginator = Paginator(laptopdata_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(data,many=True,context=serializer_context)
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

    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ApplincesASC(request):
    try:

        data_all = Applinces.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(data,many=True,context=serializer_context)
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

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_OfficeItemsASC(request):
    try:

        data_all = OfficeSupply.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(data,many=True,context=serializer_context)
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

    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getAll_HealthDESC(request):
    try:

        data_all = HealthandFitness.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(data,many=True,context=serializer_context)
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

    except HealthandFitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_HealthASC(request):
    try:

        data_all = HealthandFitness.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Health_Serializer(data,many=True,context=serializer_context)
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

    except HealthandFitness.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_MoviesASC(request):
    try:

        data_all = Movies.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(data,many=True,context=serializer_context)
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

    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_softwareASC(request):
    try:

        data_all = ComputerSoftware.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(data,many=True,context=serializer_context)
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

    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ToysASC(request):
    try:

        data_all = Toys.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(data,many=True,context=serializer_context)
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

    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAll_AudioASC(request):
    try:

        data_all = Audio.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(data,many=True,context=serializer_context)
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

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAll_SmartHomesASC(request):
    try:

        data_all = SmartHomes.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(data,many=True,context=serializer_context)
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

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getAll_CarsElectronicsASC(request):
    try:

        data_all = CarsElectronics.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(data,many=True,context=serializer_context)
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

    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])

def getAll_CamsASC(request):
    try:

        data_all = Cams.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(data,many=True,context=serializer_context)
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

    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_videoGamesASC(request):
    try:

        data_all = VideoGames.objects.all().order_by('SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(data,many=True,context=serializer_context)
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

    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_TVASC(request):
    try:

        laptopdata_all = TV.objects.all().order_by('SNR_Price')
        paginator = Paginator(laptopdata_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(data,many=True,context=serializer_context)
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

    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ApplincesDESC(request):
    try:

        data_all = Applinces.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Applinces_Serializer(data,many=True,context=serializer_context)
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

    except Applinces.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_OfficeItemsDESC(request):
    try:

        data_all = OfficeSupply.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Office_Serializer(data,many=True,context=serializer_context)
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

    except OfficeSupply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_MoviesDESC(request):
    try:

        data_all = Movies.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Movies_Serializer(data,many=True,context=serializer_context)
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

    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def getAll_softwareDESC(request):
    try:

        data_all = ComputerSoftware.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Software_Serializer(data,many=True,context=serializer_context)
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

    except ComputerSoftware.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_ToysDESC(request):
    try:

        data_all = Toys.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Toys_Serializer(data,many=True,context=serializer_context)
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

    except Toys.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAll_AudioDESC(request):
    try:

        data_all = Audio.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Audio_Serializer(data,many=True,context=serializer_context)
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

    except Audio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAll_SmartHomesDESC(request):
    try:

        data_all = SmartHomes.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Smarthomes_Serializer(data,many=True,context=serializer_context)
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

    except SmartHomes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def getAll_CarsElectronicsDESC(request):
    try:

        data_all = CarsElectronics.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = CarsElec_Serializer(data,many=True,context=serializer_context)
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

    except CarsElectronics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])

def getAll_CamsDESC(request):
    try:

        data_all = Cams.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = Cams_Serializer(data,many=True,context=serializer_context)
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

    except Cams.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_videoGamesDESC(request):
    try:

        data_all = VideoGames.objects.all().order_by('-SNR_Price')
        paginator = Paginator(data_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = VideoGames_Serializer(data,many=True,context=serializer_context)
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

    except VideoGames.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getAll_TVDESC(request):
    try:

        laptopdata_all = TV.objects.all().order_by('-SNR_Price')
        paginator = Paginator(laptopdata_all, 12)
        page = request.GET.get('page')
        try:

              data = paginator.page(page)
        except PageNotAnInteger:


            data = paginator.page(1)
        except EmptyPage:

            data = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = TV_Serializer(data,many=True,context=serializer_context)
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

    except TV.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_TV(request):

    if request.method == 'POST':

        serializer = TV_Serializer(data=request.data)
        # print serializer

        if serializer.is_valid():
            #serializer.save();


            mydata = serializer.validated_data

            # walmart.TV_Walmart()
            # amz=amazon.AmazonAPI()
            # amz.amazonTV(mydata)
            bestBuy= best.bestbuy()
            bestBuy.getTVS(mydata)

            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayTV(mydata)
            #
            #
            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartTV2(mydata)
            #
            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartTV1(mydata)

            # group=groupon.GroupOnAPI()
            # group.groupTV(mydata)
            #




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


# Create your views here.
@api_view(['POST'])
def add_Cams(request):

    if request.method == 'POST':

        serializer = Cams_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            #walmart.laptop_Walmart()
            bestBuy= best.bestbuy()
            bestBuy.getCams(mydata)

            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayCams(mydata)
            # grouponapi = groupon.GroupOnAPI()
            # grouponapi.groupCams(mydata)
            # amz=amazon.AmazonAPI()
            # amz.amazonCams(mydata)



            # walmart.Cams_Walmart()
            #
            # walmartapi= walmart.WalmartAPI()
            # walmartapi.walmartCamera(mydata)

            #atnt= ATnT.ATNT()
            #atnt.getLaptops(mydata)




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


# Create your views here.



@api_view(['POST'])
def add_CarsElectronics(request):

    if request.method == 'POST':

        serializer = CarsElec_Serializer(data=request.data)


        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data


            # amz=amazon.AmazonAPI()
            # amz.amazonCarsElectronics(mydata)
            # #walmart.laptop_Walmart()

            bestBuy= best.bestbuy()
            bestBuy.getCarsElect(mydata)

            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayCars(mydata)

            # walmartdata=walmart.WalmartAPI()
            # walmartdata.walmartCarsElec(mydata)
            #
            # grouponapi = groupon.GroupOnAPI()
            # grouponapi.groupCarsElectronics(mydata)
            #
            #
            #

            #atnt= ATnT.ATNT()
            #atnt.getLaptops(mydata)




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


# Create your views here.


@api_view(['POST'])
def add_VideoGames(request):

    if request.method == 'POST':

        serializer = VideoGames_Serializer(data=request.data)
        print serializer

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            # amz=amazon.AmazonAPI()
            # amz.amazonVideoGames(mydata)

            #
            # walmart.games_Walmart()
            bestBuy= best.bestbuy()
            bestBuy.getVideoGames(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayVideo(mydata)
            #
            # walmartdata=walmart.WalmartAPI()
            # walmartdata.walmartVideoGame(mydata)

            # group=groupon.GroupOnAPI()
            # group.groupGames(mydata)





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


# Create your views here.
@api_view(['POST'])
def add_Toys(request):

    if request.method == 'POST':

        serializer = Toys_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            #walmart.laptop_Walmart()
            bestBuy= best.bestbuy()
            bestBuy.getToys(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayToys(mydata)
            #
            # walmartdata=walmart.WalmartAPI()
            # walmartdata.walmartToys(mydata)
            #
            # group=groupon.GroupOnAPI()
            # group.groupToys(mydata)
            #
            # amz=amazon.AmazonAPI()
            # amz.amazonToys(mydata)



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


# Create your views here.


@api_view(['POST'])
def add_SmartHomes(request):

    if request.method == 'POST':

        serializer = Smarthomes_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            #walmart.laptop_Walmart()
            # bestBuy= best.bestbuy()
            # bestBuy.getSmartHomes(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebaySmarthome(mydata)
            # group=groupon.GroupOnAPI()
            # group.groupHome(mydata)

            #atnt= ATnT.ATNT()
            #atnt.getLaptops(mydata)




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


# Create your views here.



@api_view(['POST'])
def add_Audio(request):

    if request.method == 'POST':

        serializer = Audio_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            # walmart.audio_Walmart()
            bestBuy= best.bestbuy()
            bestBuy.getAudios(mydata)

            # amz=amazon.AmazonAPI()
            # amz.amazonAudio(mydata)
            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayAudio(mydata)
            #
            # walmartapi = walmart.WalmartAPI()
            # walmartapi.walmartAudio(mydata)
            # group=groupon.GroupOnAPI()
            # group.groupAudio(mydata)


            # walmart.search(mydata)
            #
            # ebay.search(mydata)
            # ebay.search(mydata)
            # ebay.search(mydata)
            #
            # best.search(mydata)

            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Create your views here.



@api_view(['POST'])
def add_Applinces(request):

    if request.method == 'POST':

        serializer = Applinces_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            # walmart.appliances_Walmart()
            # bestBuy= best.bestbuy()
            # bestBuy.getApplinces(mydata)
            amz=amazon.AmazonAPI()
            amz.amazonAppliances(mydata)



            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayApplinces(mydata)
            # #
            # walmartapi= walmart.WalmartAPI()
            # walmartapi.walmartApplinces(mydata)

            # group=groupon.GroupOnAPI()
            # group.groupAppliances(mydata)

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


# Create your views here.

@api_view(['POST'])
def add_Movies(request):

    if request.method == 'POST':

        serializer = Movies_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            #walmart.laptop_Walmart()
            bestBuy= best.bestbuy()
            bestBuy.getMovies(mydata)

            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebayMovies(mydata)


            # walmartapi= walmart.WalmartAPI()
            # walmartapi.walmartMovies(mydata)
            #
            # group= groupon.GroupOnAPI()
            # group.groupMovies(mydata)

            amz=amazon.AmazonAPI()
            amz.amazonMovies(mydata);





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


# Create your views here.



@api_view(['POST'])
def add_software(request):

    if request.method == 'POST':

        serializer = Software_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data

            # walmart.software_Walmart()
            # bestBuy= best.bestbuy()
            # bestBuy.getsoftware(mydata)
            amz=amazon.AmazonAPI()
            amz.amazonSoftware(mydata)

            # ebayapi = ebay.EbayAPI()
            # ebayapi.ebaySoftware(mydata)
            #
            # walmartdata=walmart.WalmartAPI()
            # walmartdata.walmartSoftware(mydata)
            # group=groupon.GroupOnAPI()
            # group.groupSoftware(mydata)
            #

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



@api_view(['POST'])
def add_Office(request):

    if request.method == 'POST':

        serializer = Office_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data


            # walmart.Office_Walmart()
            # bestBuy= best.bestbuy()
            # bestBuy.getOfficeSupply(mydata)

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayOffice(mydata)

            #atnt= ATnT.ATNT()
            #atnt.getLaptops(mydata)

            # group=groupon.GroupOnAPI()
            # group.groupOffice(mydata)





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



@api_view(['POST'])
def add_Health(request):

    if request.method == 'POST':

        serializer = Health_Serializer(data=request.data)

        if serializer.is_valid():
            #serializer.save();

            mydata = serializer.validated_data


            # walmart.Office_Walmart()

            ebayapi = ebay.EbayAPI()
            ebayapi.ebayHealth(mydata)

            #atnt= ATnT.ATNT()
            #atnt.getLaptops(mydata)

            # group=groupon.GroupOnAPI()
            # group.groupOffice(mydata)





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

