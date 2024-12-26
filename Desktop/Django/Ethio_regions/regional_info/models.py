from django.db import models

class Regional_info(models.Model):
    region_number= models.PositiveSmallIntegerField (null= False)
    name= models.CharField(max_length = 200)
    population_size = models.PositiveBigIntegerField(null= False)
    Area= models.FloatField(null= False)
    Capital_city = models. CharField(max_length= 300)
    Flag= models.ImageField(upload_to='Flag')
    email_address= models.EmailField(null=False)
    map = models.ImageField(upload_to ='map')
    website= models.URLField(null=False)