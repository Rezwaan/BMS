from django.conf.urls import url

from .  import views

urlpatterns = [

    url(r'^tvASC$',views.getAll_TVASC,name=""),
    url(r'^camsASC$', views.getAll_CamsASC, name=""),
    url(r'^carelectronicsASC$', views.getAll_CarsElectronicsASC, name=""),
    url(r'^videogamesASC$', views.getAll_videoGamesASC, name=""),
    url(r'^toysASC$', views.getAll_ToysASC, name=""),
    url(r'^smarthomeASC$', views.getAll_SmartHomesASC, name=""),
    url(r'^audioASC$', views.getAll_AudioASC, name=""),
    url(r'^softwareASC$', views.getAll_softwareASC, name=""),
    url(r'^applincesASC$', views.getAll_ApplincesASC, name=""),
    url(r'^moviesASC$', views.getAll_MoviesASC, name=""),
    url(r'^officeASC$', views.getAll_OfficeItemsASC, name=""),

    url(r'^tvDESC$', views.getAll_TVDESC, name=""),
    url(r'^camsDESC$', views.getAll_CamsDESC, name=""),
    url(r'^carelectronicsDESC$', views.getAll_CarsElectronicsDESC, name=""),
    url(r'^videogamesDESC$', views.getAll_videoGamesDESC, name=""),
    url(r'^toysDESC$', views.getAll_ToysDESC, name=""),
    url(r'^smarthomeDESC$', views.getAll_SmartHomesDESC, name=""),
    url(r'^audioDESC$', views.getAll_AudioDESC, name=""),
    url(r'^softwareDESC$', views.getAll_softwareDESC, name=""),
    url(r'^applincesDESC$', views.getAll_ApplincesDESC, name=""),
    url(r'^moviesDESC$', views.getAll_MoviesDESC, name=""),
    url(r'^officeDESC$', views.getAll_OfficeItemsDESC, name=""),

    url(r'^health/add$', views.add_Health, name=""),
    url(r'^health$', views.getAll_Health, name=""),
    url(r'^healthASC$', views.getAll_HealthASC, name=""),
    url(r'^healthDESC$', views.getAll_HealthDESC, name=""),

    url(r'^tv$', views.getAll_TV, name=""),
    url(r'^tv/add$', views.add_TV, name=""),
    url(r'^cams$', views.getAll_Cams, name=""),
    url(r'^cams/add$', views.add_Cams, name=""),
    url(r'^carelectronics$', views.getAll_CarsElectronics, name=""),
    url(r'^carelectronics/add$', views.add_CarsElectronics, name=""),
    url(r'^videogames$', views.getAll_videoGames, name=""),
    url(r'^videogames/add$', views.add_VideoGames, name=""),
    url(r'^toys$', views.getAll_Toys, name=""),
    url(r'^toys/add$', views.add_Toys, name=""),
    url(r'^smarthome$', views.getAll_SmartHomes, name=""),
    url(r'^smarthome/add$', views.add_SmartHomes, name=""),
    url(r'^audio$', views.getAll_Audio, name=""),
    url(r'^audio/add$', views.add_Audio, name=""),
    url(r'^software$', views.getAll_software, name=""),
    url(r'^software/add$', views.add_software, name=""),
    url(r'^applinces$', views.getAll_Applinces, name=""),
    url(r'^applinces/add$', views.add_Applinces, name=""),
    url(r'^movies$', views.getAll_Movies, name=""),
    url(r'^movies/add$', views.add_Movies, name=""),
    url(r'^office$', views.getAll_OfficeItems, name=""),
    url(r'^office/add$', views.add_Office, name=""),

    url(r'^office/models$', views.getModelsOffice, name=""),#
    url(r'^health/models$', views.getModelsHealth, name=""),#
    url(r'^movies/models$', views.getModelsMovies, name=""),#
    url(r'^toys/models$', views.getModelsToys, name=""),#
    url(r'^applinces/models$', views.getModelsApplinces, name=""),#
    url(r'^audio/models$', views.getModelsAudio, name=""),#
    url(r'^tv/models$', views.getModelsTV, name=""),#
    url(r'^cams/models$', views.getModelsCams, name=""),#
    url(r'^cars/models$', views.getModelsCarElec, name=""),#
    url(r'^video/models$', views.getModelsGames, name=""),#
    url(r'^smarthome/models$', views.getModelsSmarthome, name=""),#
    url(r'^software/models$', views.getModelsSoftware, name=""),#

    # url(r'^filterlaptop/(?P<query>.+)/$', views.FilterLaptops,name="Filter"),


    url(r'^filterhealth/(?P<query>.+)/$', views.Filter_Health, name="Filter"),

    url(r'^filterhealthASC/(?P<query>.+)/$', views.Filter_HealthASC, name="Filter"),
    url(r'^filterhealthDESC/(?P<query>.+)/$', views.Filter_HealthDESC, name="Filter"),
    url(r'^filterappliences/(?P<query>.+)/$', views.Filter_Appliences, name="Filter"),
    url(r'^filtergames/(?P<query>.+)/$', views.Filter_videogames, name="Filter"),
    url(r'^filteraudio/(?P<query>.+)/$', views.Filter_audio, name="Filter"),
    url(r'^filtertv/(?P<query>.+)/$', views.Filter_tv, name="Filter"),
    url(r'^filtertoys/(?P<query>.+)/$', views.Filter_toys, name="Filter"),
    url(r'^filtersoftware/(?P<query>.+)/$', views.Filter_software, name="Filter"),
    url(r'^filterofficesupply/(?P<query>.+)/$', views.Filter_office, name="Filter"),
    url(r'^filtersmarthomes/(?P<query>.+)/$', views.Filter_smarthome, name="Filter"),
    url(r'^filtercams/(?P<query>.+)/$', views.Filter_cams, name="Filter"),
    url(r'^filtermovies/(?P<query>.+)/$', views.Filter_movies, name="Filter"),
    url(r'^filtercarselectronics/(?P<query>.+)/$', views.Filter_carselectronics, name="Filter"),

    url(r'^filterappliencesASC/(?P<query>.+)/$', views.Filter_AppliencesASC, name="Filter"),
    url(r'^filtergamesASC/(?P<query>.+)/$', views.Filter_videogamesASC, name="Filter"),
    url(r'^filteraudioASC/(?P<query>.+)/$', views.Filter_audioASC, name="Filter"),
    url(r'^filtertvASC/(?P<query>.+)/$', views.Filter_tvASC, name="Filter"),
    url(r'^filtertoysASC/(?P<query>.+)/$', views.Filter_toysASC, name="Filter"),
    url(r'^filtersoftwareASC/(?P<query>.+)/$', views.Filter_softwareASC, name="Filter"),
    url(r'^filterofficesupplyASC/(?P<query>.+)/$', views.Filter_officeASC, name="Filter"),
    url(r'^filtersmarthomesASC/(?P<query>.+)/$', views.Filter_smarthomeASC, name="Filter"),
    url(r'^filtercamsASC/(?P<query>.+)/$', views.Filter_camsASC, name="Filter"),
    url(r'^filtermoviesASC/(?P<query>.+)/$', views.Filter_moviesASC, name="Filter"),
    url(r'^filtercarselectronicsASC/(?P<query>.+)/$', views.Filter_carselectronicsASC, name="Filter"),

    url(r'^filterappliencesDESC/(?P<query>.+)/$', views.Filter_AppliencesDESC, name="Filter"),
    url(r'^filtergamesDESC/(?P<query>.+)/$', views.Filter_videogamesDESC, name="Filter"),
    url(r'^filteraudioDESC/(?P<query>.+)/$', views.Filter_audioDESC, name="Filter"),
    url(r'^filtertvDESC/(?P<query>.+)/$', views.Filter_tvDESC, name="Filter"),
    url(r'^filtertoysDESC/(?P<query>.+)/$', views.Filter_toysDESC, name="Filter"),
    url(r'^filtersoftwareDESC/(?P<query>.+)/$', views.Filter_softwareDESC, name="Filter"),
    url(r'^filterofficesupplyDESC/(?P<query>.+)/$', views.Filter_officeDESC, name="Filter"),
    url(r'^filtersmarthomesDESC/(?P<query>.+)/$', views.Filter_smarthomeDESC, name="Filter"),
    url(r'^filtercamsDESC/(?P<query>.+)/$', views.Filter_camsDESC, name="Filter"),
    url(r'^filtermoviesDESC/(?P<query>.+)/$', views.Filter_moviesDESC, name="Filter"),
    url(r'^filtercarselectronicsDESC/(?P<query>.+)/$', views.Filter_carselectronicsDESC, name="Filter"),

]