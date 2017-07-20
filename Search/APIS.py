
from rest_framework.decorators import api_view
from rest_framework.response import Response    # to send specific response
from rest_framework import status
from products.models import TV,Cams,CarsElectronics,VideoGames,Toys,SmartHomes,Audio,ComputerSoftware,Applinces,Movies,OfficeSupply,HealthandFitness

from products.serializers import TV_Serializer,Cams_Serializer,CarsElec_Serializer,VideoGames_Serializer,\
    Toys_Serializer,Smarthomes_Serializer,Audio_Serializer,Software_Serializer, Applinces_Serializer,Movies_Serializer,Office_Serializer,Health_Serializer,\
    TV_SerializerTitle,Cams_SerializerTitle,CarsElec_SerializerTitle,VideoGames_SerializerTitle,Toys_SerializerTitle,Smarthomes_SerializerTitle,Audio_SerializerTitle,Software_SerializerTitle,Applinces_SerializerTitle,Health_SerializerTitle,Office_SerializerTitle,Movies_SerializerTitle

from laptop.models import Laptop_DB
from laptop.serializers import Laptop_Serializer,Laptop_SerializerTitle
from mobile.models import Mobile_DB
from mobile.serializer import Mobile_Serializer,Mobile_SerializerTitle
from wearables.models import Wearable_DB
from wearables.serializers import Wearable_Serializer,Wearable_SerializerTitle

from itertools import chain

# Create your views here.
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@api_view(['GET'])
def CountQueryAll(request,query):
    try:
        que = Q(SNR_Title__icontains=query) | Q(SNR_ProductURL__icontains=query ) |Q(SNR_ModelNo__icontains=query) | Q(
            SNR_Available__icontains=query) | Q(SNR_UPC__icontains=query)

        LaptopCount = Laptop_DB.objects.filter(que).count()
        MobileCount = Mobile_DB.objects.filter(que).count()
        WearableCount = Wearable_DB.objects.filter(que).count()
        ApplincesCount = Applinces.objects.filter(que).count()
        softwareCount = ComputerSoftware.objects.filter(que).count()
        smarthomesCount = SmartHomes.objects.filter(que).count()
        videogamesCount = VideoGames.objects.filter(que).count()
        audioCount = Audio.objects.filter(que).count()
        moviesCount = Movies.objects.filter(que).count()
        CarsElecCount = CarsElectronics.objects.filter(que).count()
        OfficeCount = OfficeSupply.objects.filter(que).count()
        toysCount = Toys.objects.filter(que).count()
        TVCount = TV.objects.filter(que).count()
        CamsCount = Cams.objects.filter(que).count()
        healthCount=HealthandFitness.objects.filter(que).count()


    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        # serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response({'laptop':LaptopCount,
                         'mobile':MobileCount,'wearable':WearableCount,'software':softwareCount,'appliances':ApplincesCount,
                         'smarthome':smarthomesCount,'videogames':videogamesCount,'audio':audioCount,'movies':moviesCount,
                         'carselectronic':CarsElecCount, 'office':OfficeCount, 'toys':toysCount,'tv':TVCount,
                         'cams':CamsCount,
                         'Health':healthCount})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def CountAll(request):
    try:
        LaptopCount = Laptop_DB.objects.all().count()
        MobileCount = Mobile_DB.objects.all().count()
        WearableCount = Wearable_DB.objects.all().count()
        ApplincesCount = Applinces.objects.all().count()
        softwareCount = ComputerSoftware.objects.all().count()
        smarthomesCount = SmartHomes.objects.all().count()
        videogamesCount = VideoGames.objects.all().count()
        audioCount = Audio.objects.all().count()
        moviesCount = Movies.objects.all().count()
        CarsElecCount = CarsElectronics.objects.all().count()
        OfficeCount = OfficeSupply.objects.all().count()
        toysCount = Toys.objects.all().count()
        TVCount = TV.objects.all().count()
        CamsCount = Cams.objects.all().count()
        healthCount=HealthandFitness.objects.all().count()


    except Mobile_DB.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        # serializer = Mobile_Serializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response({'laptop':LaptopCount,
                         'mobile':MobileCount,'wearable':WearableCount,'software':softwareCount,'appliances':ApplincesCount,
                         'smarthome':smarthomesCount,'videogames':videogamesCount,'audio':audioCount,'movies':moviesCount,
                         'carselectronic':CarsElecCount, 'office':OfficeCount, 'toys':toysCount,'tv':TVCount,
                         'cams':CamsCount,
                         'Health':healthCount})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass



@api_view(['GET'])
def FilterGroupon(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_ProductURL__icontains=query ) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       Mobile_all = Mobile_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       Wearable_all = Wearable_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       Applinces_data=Applinces.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       software_data=ComputerSoftware.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       smarthomes_data=SmartHomes.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       videogames_data=VideoGames.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       audio_data=Audio.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       movies_data=Movies.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       CarsElec_data=CarsElectronics.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       Office_data=OfficeSupply.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       toys_data=Toys.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       TV_data=TV.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       Cams_data=Cams.objects.filter(que).filter(SNR_Available__icontains="Groupon")
       Health_data = HealthandFitness.objects.filter(que).filter(SNR_Available__icontains="Groupon")

       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_seri=Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data or health_seri.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterGrouponASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_ProductURL__icontains=query ) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       Mobile_all = Mobile_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       Wearable_all = Wearable_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       Applinces_data=Applinces.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       software_data=ComputerSoftware.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       smarthomes_data=SmartHomes.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       videogames_data=VideoGames.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       audio_data=Audio.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       movies_data=Movies.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       CarsElec_data=CarsElectronics.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       Office_data=OfficeSupply.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       toys_data=Toys.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       TV_data=TV.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       Cams_data=Cams.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')
       Health_data = HealthandFitness.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('SNR_Price')


       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_seri=Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data or health_seri.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterGrouponDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_ProductURL__icontains=query ) |  Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       Mobile_all = Mobile_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       Wearable_all = Wearable_DB.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       Applinces_data=Applinces.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       software_data=ComputerSoftware.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       smarthomes_data=SmartHomes.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       videogames_data=VideoGames.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       audio_data=Audio.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       movies_data=Movies.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       CarsElec_data=CarsElectronics.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       Office_data=OfficeSupply.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       toys_data=Toys.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       TV_data=TV.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       Cams_data=Cams.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')
       health_data=HealthandFitness.objects.filter(que).filter(SNR_Available__icontains="Groupon").order_by('-SNR_Price')

       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_Serializer = Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data or health_Serializer.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterLaptopsbyModelUPC(request,query):

   print(query)
   try:
       que =  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que)
       Mobile_all = Mobile_DB.objects.filter(que)
       Wearable_all = Wearable_DB.objects.filter(que)
       Applinces_data=Applinces.objects.filter(que)
       software_data=ComputerSoftware.objects.filter(que)
       smarthomes_data=SmartHomes.objects.filter(que)
       videogames_data=VideoGames.objects.filter(que)
       audio_data=Audio.objects.filter(que)
       movies_data=Movies.objects.filter(que)
       CarsElec_data=CarsElectronics.objects.filter(que)
       Office_data=OfficeSupply.objects.filter(que)
       toys_data=Toys.objects.filter(que)
       TV_data=TV.objects.filter(que)
       Cams_data=Cams.objects.filter(que)
       Health_data=HealthandFitness.objects.filter(que)

       LaptopCount = Laptop_DB.objects.filter(que).count()
       MobileCount= Mobile_DB.objects.filter(que).count()
       WearableCount = Wearable_DB.objects.filter(que).count()
       ApplincesCount=Applinces.objects.filter(que).count()
       softwareCount=ComputerSoftware.objects.filter(que).count()
       smarthomesCount=SmartHomes.objects.filter(que).count()
       videogamesCount=VideoGames.objects.filter(que).count()
       audioCount=Audio.objects.filter(que).count()
       moviesCount=Movies.objects.filter(que).count()
       CarsElecCount=CarsElectronics.objects.filter(que).count()
       OfficeCount=OfficeSupply.objects.filter(que).count()
       toysCount=Toys.objects.filter(que).count()
       TVCount=TV.objects.filter(que).count()
       CamsCount = Cams.objects.filter(que).count()
       HealthCount = HealthandFitness.objects.filter(que).count()

       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_Serializer = Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
           'laptop': LaptopCount,
           'mobile': MobileCount, 'wearable': WearableCount, 'software': softwareCount, 'appliances': ApplincesCount,
           'smarthome': smarthomesCount, 'videogames': videogamesCount, 'audio': audioCount, 'movies': moviesCount,
           'carselectronic': CarsElecCount, 'office': OfficeCount, 'toys': toysCount, 'tv': TVCount,
           'cams': CamsCount,
           'health': HealthCount,
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
or health_Serializer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterLaptopsbyModelUPCDESC(request,query):

   print(query)
   try:
       que =  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).order_by('-SNR_Price')
       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       Wearable_all = Wearable_DB.objects.filter(que).order_by('-SNR_Price')
       Applinces_data=Applinces.objects.filter(que).order_by('-SNR_Price')
       software_data=ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
       smarthomes_data=SmartHomes.objects.filter(que).order_by('-SNR_Price')
       videogames_data=VideoGames.objects.filter(que).order_by('-SNR_Price')
       audio_data=Audio.objects.filter(que).order_by('-SNR_Price')
       movies_data=Movies.objects.filter(que).order_by('-SNR_Price')
       CarsElec_data=CarsElectronics.objects.filter(que).order_by('-SNR_Price')
       Office_data=OfficeSupply.objects.filter(que).order_by('-SNR_Price')
       toys_data=Toys.objects.filter(que).order_by('-SNR_Price')
       TV_data=TV.objects.filter(que).order_by('-SNR_Price')
       Cams_data=Cams.objects.filter(que).order_by('-SNR_Price')
       Health_data=HealthandFitness.objects.filter(que).order_by('-SNR_Price')

       LaptopCount = Laptop_DB.objects.filter(que).count()
       MobileCount= Mobile_DB.objects.filter(que).count()
       WearableCount = Wearable_DB.objects.filter(que).count()
       ApplincesCount=Applinces.objects.filter(que).count()
       softwareCount=ComputerSoftware.objects.filter(que).count()
       smarthomesCount=SmartHomes.objects.filter(que).count()
       videogamesCount=VideoGames.objects.filter(que).count()
       audioCount=Audio.objects.filter(que).count()
       moviesCount=Movies.objects.filter(que).count()
       CarsElecCount=CarsElectronics.objects.filter(que).count()
       OfficeCount=OfficeSupply.objects.filter(que).count()
       toysCount=Toys.objects.filter(que).count()
       TVCount=TV.objects.filter(que).count()
       CamsCount=Cams.objects.filter(que).count()
       HealthCount=HealthandFitness.objects.filter(que).count()


       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_seri = Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
           'laptop': LaptopCount,
           'mobile': MobileCount, 'wearable': WearableCount, 'software': softwareCount, 'appliances': ApplincesCount,
           'smarthome': smarthomesCount, 'videogames': videogamesCount, 'audio': audioCount, 'movies': moviesCount,
           'carselectronic': CarsElecCount, 'office': OfficeCount, 'toys': toysCount, 'tv': TVCount,
           'cams': CamsCount,
       'totalItems':items,
           'health':HealthCount,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
           or health_seri.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterLaptopsbyModelUPCASC(request,query):

   print(query)
   try:
       que =  Q(SNR_ModelNo__icontains=query) |Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).order_by('SNR_Price')
       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       Wearable_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
       Applinces_data=Applinces.objects.filter(que).order_by('SNR_Price')
       software_data=ComputerSoftware.objects.filter(que).order_by('SNR_Price')
       smarthomes_data=SmartHomes.objects.filter(que).order_by('SNR_Price')
       videogames_data=VideoGames.objects.filter(que).order_by('SNR_Price')
       audio_data=Audio.objects.filter(que).order_by('SNR_Price')
       movies_data=Movies.objects.filter(que).order_by('SNR_Price')
       CarsElec_data=CarsElectronics.objects.filter(que).order_by('SNR_Price')
       Office_data=OfficeSupply.objects.filter(que).order_by('SNR_Price')
       toys_data=Toys.objects.filter(que).order_by('SNR_Price')
       TV_data=TV.objects.filter(que).order_by('SNR_Price')
       Cams_data=Cams.objects.filter(que).order_by('SNR_Price')
       Health_data=HealthandFitness.objects.filter(que).order_by('SNR_Price')

       LaptopCount = Laptop_DB.objects.filter(que).count()
       MobileCount= Mobile_DB.objects.filter(que).count()
       WearableCount = Wearable_DB.objects.filter(que).count()
       ApplincesCount=Applinces.objects.filter(que).count()
       softwareCount=ComputerSoftware.objects.filter(que).count()
       smarthomesCount=SmartHomes.objects.filter(que).count()
       videogamesCount=VideoGames.objects.filter(que).count()
       audioCount=Audio.objects.filter(que).count()
       moviesCount=Movies.objects.filter(que).count()
       CarsElecCount=CarsElectronics.objects.filter(que).count()
       OfficeCount=OfficeSupply.objects.filter(que).count()
       toysCount=Toys.objects.filter(que).count()
       TVCount=TV.objects.filter(que).count()
       CamsCount=Cams.objects.filter(que).count()
       HealthCount=HealthandFitness.objects.filter(que).count()


       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_Serializer = Health_Serializer(data, many=True, context=serializer_context)


# res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
           'laptop': LaptopCount,
           'mobile': MobileCount, 'wearable': WearableCount, 'software': softwareCount, 'appliances': ApplincesCount,
           'smarthome': smarthomesCount, 'videogames': videogamesCount, 'audio': audioCount, 'movies': moviesCount,
           'carselectronic': CarsElecCount, 'office': OfficeCount, 'toys': toysCount, 'tv': TVCount,
           'cams': CamsCount,
           'Health':HealthCount,
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
                or health_Serializer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


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
def FilterLaptops(request,query):

   print(query)
   try:
       que = Q(SNR_ProductURL__icontains=query ) |Q(SNR_ProductURL__icontains=query ) |   Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que)
       Mobile_all = Mobile_DB.objects.filter(que)
       Wearable_all = Wearable_DB.objects.filter(que)
       Applinces_data=Applinces.objects.filter(que)
       software_data=ComputerSoftware.objects.filter(que)
       smarthomes_data=SmartHomes.objects.filter(que)
       videogames_data=VideoGames.objects.filter(que)
       audio_data=Audio.objects.filter(que)
       movies_data=Movies.objects.filter(que)
       CarsElec_data=CarsElectronics.objects.filter(que)
       Office_data=OfficeSupply.objects.filter(que)
       toys_data=Toys.objects.filter(que)
       TV_data=TV.objects.filter(que)
       Cams_data=Cams.objects.filter(que)
       Health_data=HealthandFitness.objects.filter(que)

       LaptopCount = Laptop_DB.objects.filter(que).count()
       MobileCount= Mobile_DB.objects.filter(que).count()
       WearableCount = Wearable_DB.objects.filter(que).count()
       ApplincesCount=Applinces.objects.filter(que).count()
       softwareCount=ComputerSoftware.objects.filter(que).count()
       smarthomesCount=SmartHomes.objects.filter(que).count()
       videogamesCount=VideoGames.objects.filter(que).count()
       audioCount=Audio.objects.filter(que).count()
       moviesCount=Movies.objects.filter(que).count()
       CarsElecCount=CarsElectronics.objects.filter(que).count()
       OfficeCount=OfficeSupply.objects.filter(que).count()
       toysCount=Toys.objects.filter(que).count()
       TVCount=TV.objects.filter(que).count()
       CamsCount = Cams.objects.filter(que).count()
       HealthCount = HealthandFitness.objects.filter(que).count()

       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_Serializer = Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
           'laptop': LaptopCount,
           'mobile': MobileCount, 'wearable': WearableCount, 'software': softwareCount, 'appliances': ApplincesCount,
           'smarthome': smarthomesCount, 'videogames': videogamesCount, 'audio': audioCount, 'movies': moviesCount,
           'carselectronic': CarsElecCount, 'office': OfficeCount, 'toys': toysCount, 'tv': TVCount,
           'cams': CamsCount,
           'health': HealthCount,
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
or health_Serializer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterLaptopsDESC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_ProductURL__icontains=query ) | Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).order_by('-SNR_Price')
       Mobile_all = Mobile_DB.objects.filter(que).order_by('-SNR_Price')
       Wearable_all = Wearable_DB.objects.filter(que).order_by('-SNR_Price')
       Applinces_data=Applinces.objects.filter(que).order_by('-SNR_Price')
       software_data=ComputerSoftware.objects.filter(que).order_by('-SNR_Price')
       smarthomes_data=SmartHomes.objects.filter(que).order_by('-SNR_Price')
       videogames_data=VideoGames.objects.filter(que).order_by('-SNR_Price')
       audio_data=Audio.objects.filter(que).order_by('-SNR_Price')
       movies_data=Movies.objects.filter(que).order_by('-SNR_Price')
       CarsElec_data=CarsElectronics.objects.filter(que).order_by('-SNR_Price')
       Office_data=OfficeSupply.objects.filter(que).order_by('-SNR_Price')
       toys_data=Toys.objects.filter(que).order_by('-SNR_Price')
       TV_data=TV.objects.filter(que).order_by('-SNR_Price')
       Cams_data=Cams.objects.filter(que).order_by('-SNR_Price')
       Health_data=HealthandFitness.objects.filter(que).order_by('-SNR_Price')

       LaptopCount = Laptop_DB.objects.filter(que).count()
       MobileCount= Mobile_DB.objects.filter(que).count()
       WearableCount = Wearable_DB.objects.filter(que).count()
       ApplincesCount=Applinces.objects.filter(que).count()
       softwareCount=ComputerSoftware.objects.filter(que).count()
       smarthomesCount=SmartHomes.objects.filter(que).count()
       videogamesCount=VideoGames.objects.filter(que).count()
       audioCount=Audio.objects.filter(que).count()
       moviesCount=Movies.objects.filter(que).count()
       CarsElecCount=CarsElectronics.objects.filter(que).count()
       OfficeCount=OfficeSupply.objects.filter(que).count()
       toysCount=Toys.objects.filter(que).count()
       TVCount=TV.objects.filter(que).count()
       CamsCount=Cams.objects.filter(que).count()
       HealthCount=HealthandFitness.objects.filter(que).count()


       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_seri = Health_Serializer(data, many=True, context=serializer_context)


        # res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
           'laptop': LaptopCount,
           'mobile': MobileCount, 'wearable': WearableCount, 'software': softwareCount, 'appliances': ApplincesCount,
           'smarthome': smarthomesCount, 'videogames': videogamesCount, 'audio': audioCount, 'movies': moviesCount,
           'carselectronic': CarsElecCount, 'office': OfficeCount, 'toys': toysCount, 'tv': TVCount,
           'cams': CamsCount,
       'totalItems':items,
           'health':HealthCount,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
           or health_seri.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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
def FilterLaptopsASC(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_ProductURL__icontains=query ) | Q(SNR_ModelNo__icontains=query) |Q(SNR_Available__icontains=query)|Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.filter(que).order_by('SNR_Price')
       Mobile_all = Mobile_DB.objects.filter(que).order_by('SNR_Price')
       Wearable_all = Wearable_DB.objects.filter(que).order_by('SNR_Price')
       Applinces_data=Applinces.objects.filter(que).order_by('SNR_Price')
       software_data=ComputerSoftware.objects.filter(que).order_by('SNR_Price')
       smarthomes_data=SmartHomes.objects.filter(que).order_by('SNR_Price')
       videogames_data=VideoGames.objects.filter(que).order_by('SNR_Price')
       audio_data=Audio.objects.filter(que).order_by('SNR_Price')
       movies_data=Movies.objects.filter(que).order_by('SNR_Price')
       CarsElec_data=CarsElectronics.objects.filter(que).order_by('SNR_Price')
       Office_data=OfficeSupply.objects.filter(que).order_by('SNR_Price')
       toys_data=Toys.objects.filter(que).order_by('SNR_Price')
       TV_data=TV.objects.filter(que).order_by('SNR_Price')
       Cams_data=Cams.objects.filter(que).order_by('SNR_Price')
       Health_data=HealthandFitness.objects.filter(que).order_by('SNR_Price')

       LaptopCount = Laptop_DB.objects.filter(que).count()
       MobileCount= Mobile_DB.objects.filter(que).count()
       WearableCount = Wearable_DB.objects.filter(que).count()
       ApplincesCount=Applinces.objects.filter(que).count()
       softwareCount=ComputerSoftware.objects.filter(que).count()
       smarthomesCount=SmartHomes.objects.filter(que).count()
       videogamesCount=VideoGames.objects.filter(que).count()
       audioCount=Audio.objects.filter(que).count()
       moviesCount=Movies.objects.filter(que).count()
       CarsElecCount=CarsElectronics.objects.filter(que).count()
       OfficeCount=OfficeSupply.objects.filter(que).count()
       toysCount=Toys.objects.filter(que).count()
       TVCount=TV.objects.filter(que).count()
       CamsCount=Cams.objects.filter(que).count()
       HealthCount=HealthandFitness.objects.filter(que).count()


       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       #list(chain(page_list, article_list, post_list))

       #
       # l_paginator = Paginator(Laptop_all, 12)
       # m_paginator = Paginator(Mobile_all, 12)
       # w_paginator = Paginator(Wearable_all, 12)
       #

       paginator = Paginator(products, 12)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_Serializer(data, many=True, context=serializer_context)
       M_Serializer = Mobile_Serializer(data, many=True, context=serializer_context)
       W_Serializer = Wearable_Serializer(data, many=True, context=serializer_context)
       App_Serializer = Applinces_Serializer(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_Serializer(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_Serializer(data, many=True, context=serializer_context)
       Tv_Serializer = TV_Serializer(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_Serializer(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_Serializer(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_Serializer(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_Serializer(data, many=True, context=serializer_context)
       soft_Serializer = Software_Serializer(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_Serializer(data, many=True, context=serializer_context)
       offic_Serializer = Office_Serializer(data, many=True, context=serializer_context)
       health_Serializer = Health_Serializer(data, many=True, context=serializer_context)


# res.update('pages_count:', paginator.num_pages())
        #return Response(res)
       items=0
       pages=0

       items=paginator._count
       pages=paginator._get_num_pages()
       res={
           'laptop': LaptopCount,
           'mobile': MobileCount, 'wearable': WearableCount, 'software': softwareCount, 'appliances': ApplincesCount,
           'smarthome': smarthomesCount, 'videogames': videogamesCount, 'audio': audioCount, 'movies': moviesCount,
           'carselectronic': CarsElecCount, 'office': OfficeCount, 'toys': toysCount, 'tv': TVCount,
           'cams': CamsCount,
           'Health':HealthCount,
       'totalItems':items,
       'totalPages':pages,
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
                or health_Serializer.data
        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:


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
def AutoComplete(request,query):

   print(query)
   try:
       que = Q(SNR_Title__icontains=query ) | Q(SNR_ModelNo__icontains=query) | Q(SNR_UPC__icontains=query)

       Laptop_all = Laptop_DB.objects.only('SNR_Title').filter(que)[:5]
       Mobile_all = Mobile_DB.objects.only('SNR_Title').filter(que)[:5]
       Wearable_all = Wearable_DB.objects.only('SNR_Title').filter(que)[:5]
       Applinces_data=Applinces.objects.only('SNR_Title').filter(que)[:5]
       software_data=ComputerSoftware.objects.only('SNR_Title').filter(que)[:5]
       smarthomes_data=SmartHomes.objects.only('SNR_Title').filter(que)[:5]
       videogames_data=VideoGames.objects.only('SNR_Title').filter(que)[:5]
       audio_data=Audio.objects.only('SNR_Title').filter(que)[:5]
       movies_data=Movies.objects.only('SNR_Title').filter(que)[:5]
       CarsElec_data=CarsElectronics.objects.only('SNR_Title').filter(que)[:5]
       Office_data=OfficeSupply.objects.only('SNR_Title').filter(que)[:5]
       toys_data=Toys.objects.only('SNR_Title').filter(que)[:5]
       TV_data=TV.objects.only('SNR_Title').filter(que)[:5]
       Cams_data=Cams.objects.only('SNR_Title').filter(que)[:5]
       Health_data=HealthandFitness.objects.only('SNR_Title').filter(que)[:5]



       products= list(chain(Laptop_all, Mobile_all, Wearable_all,Applinces_data,software_data,smarthomes_data,videogames_data,audio_data,movies_data,
                            CarsElec_data,Office_data,toys_data,TV_data,Cams_data,Health_data))
       paginator = Paginator(products, 30)


       page = request.GET.get('page')
       try:

          data = paginator.page(page)
       except PageNotAnInteger:

           data = paginator.page(1)
       except EmptyPage:

           data = paginator.page(paginator.num_pages)

       serializer_context = {'request': request}
       L_Serializer = Laptop_SerializerTitle(data, many=True, context=serializer_context)
       M_Serializer = Mobile_SerializerTitle(data, many=True, context=serializer_context)
       W_Serializer = Wearable_SerializerTitle(data, many=True, context=serializer_context)
       App_Serializer = Applinces_SerializerTitle(data, many=True, context=serializer_context)
       Cam_Serializer = Cams_SerializerTitle(data, many=True, context=serializer_context)
       Car_Serializer = CarsElec_SerializerTitle(data, many=True, context=serializer_context)
       Tv_Serializer = TV_SerializerTitle(data, many=True, context=serializer_context)
       Toy_Serializer = Toys_SerializerTitle(data, many=True, context=serializer_context)
       Aud_Serializer = Audio_SerializerTitle(data, many=True, context=serializer_context)
       Video_Serializer = VideoGames_SerializerTitle(data, many=True, context=serializer_context)
       Movi_Serializer = Movies_SerializerTitle(data, many=True, context=serializer_context)
       soft_Serializer = Software_SerializerTitle(data, many=True, context=serializer_context)
       smart_Serializer = Smarthomes_SerializerTitle(data, many=True, context=serializer_context)
       offic_Serializer = Office_SerializerTitle(data, many=True, context=serializer_context)
       health_seri = Health_SerializerTitle(data, many=True, context=serializer_context)



       items=paginator._count
       pages=paginator._get_num_pages()
       res={
       'results': L_Serializer.data or M_Serializer.data or W_Serializer.data or offic_Serializer.data or smart_Serializer.data or soft_Serializer.data or Movi_Serializer.data
           or Video_Serializer.data or Aud_Serializer.data or Toy_Serializer.data or Tv_Serializer.data or Car_Serializer.data or Cam_Serializer.data or App_Serializer.data
           or health_seri.data

        }
       return Response(res)


   except Laptop_DB.DoesNotExist or Mobile_DB.DoesNotExist or Wearable_DB.DoesNotExist:

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

