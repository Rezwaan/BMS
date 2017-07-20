from django.db import models
from time import time


def get_name(instance,filename):
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'),filename)

# Create your models here.
class Trends(models.Model):


    SNR_Title= models.CharField(max_length=500,blank=True,default="")
    SNR_AvailableAt= models.CharField(max_length=200,blank=True,default="")
    SNR_Description = models.CharField(max_length=5000, blank=True, default="")
    SNR_Type = models.CharField(max_length=200, blank=True, default="Trending")
    SNR_Category = models.CharField(max_length=200, blank=True, default="mobile")

    SNR_PriceMin= models.CharField(max_length=20,blank=True,default="")
    SNR_PriceMax= models.CharField(max_length=20,blank=True,default="")
    SNR_ProductURL= models.CharField(max_length=3000,blank=True,default="")
    SNR_ImageURL= models.CharField(max_length=3000,blank=True,default="")

    SNR_Date = models.DateTimeField(auto_now_add=True, blank=True)


    class Meta:
         unique_together = (('SNR_Title', 'SNR_ImageURL','SNR_ProductURL','SNR_PriceMax'))

    def __str__(self):
        return self.SNR_Title+' , '+str(self.SNR_Date)+' , '+str(self.SNR_Description)+' , '+self.SNR_ImageURL+' , '+self.SNR_PriceMin+' , '+self.SNR_PriceMax+' , '+self.SNR_ProductURL+' , '+self.SNR_AvailableAt+','+self.SNR_Category+','+self.SNR_Type


