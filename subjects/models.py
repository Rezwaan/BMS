from django.db import models


class pp_subjects(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_age = models.IntegerField()
    psd1 = models.FloatField()
    psd3 = models.FloatField()
    psd6 = models.FloatField()
    psd10 = models.FloatField()

    def __str__(self):
        return self.subject_name + str(self.subject_age)


