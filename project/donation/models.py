from django.db import models

# Create your models here.

class Donation(models.Model):  
    did = models.CharField(max_length=20)  
    dname = models.CharField(max_length=100)  
    dcontent = models.TextField() 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "donation"  