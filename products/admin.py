from django.contrib import admin

from .models import TV,Cams,CarsElectronics,VideoGames,Toys,SmartHomes,Audio,ComputerSoftware,Applinces,Movies,OfficeSupply
# Register your models here.

admin.site.register(TV)
admin.site.register(OfficeSupply)
admin.site.register(Movies)
admin.site.register(ComputerSoftware)
admin.site.register(Applinces)
admin.site.register(Audio)
admin.site.register(Cams)
admin.site.register(CarsElectronics)
admin.site.register(VideoGames)
admin.site.register(Toys)
admin.site.register(SmartHomes)
