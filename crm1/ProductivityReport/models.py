from django.db import models
#import model from other app
from LabourReport.models import *

# Create your models here.





class ProductivityReport(models.Model):
    # Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    # StructureName=models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    # ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    # LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    # # CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    # ContractorName=models.ForeignKey(SiteEngDay,on_delete=models.CASCADE,null=True)
    # LabourCategory=models.ForeignKey(SiteEngDay,on_delete=models.CASCADE,null=True,related_name='LabourCat')
    # CategoryName=models.ForeignKey(SiteEngDay,on_delete=models.CASCADE,null=True,related_name='CatName')
    units=[
        ('','None'),
        ('m','m'),
        ('m sq.','m sq.'),
        # subscript
        ('m cube','m cube'),
    ]
    LRid=models.IntegerField(null=True)
    Unit=models.CharField(max_length=200,null=True,choices=units)
    Length=models.IntegerField(null=True)
    Breadth=models.IntegerField(null=True)
    Depth=models.IntegerField(null=True)
    Quantity=models.IntegerField(null=True)
    def __str__(self):
        return self.LRid

class ProductivityNightReport(models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    StructureName=models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    Length=models.IntegerField(null=True,default=1)
    Breadth=models.IntegerField(null=True,default=1)
    Depth=models.IntegerField(null=True,default=1)
    Quantity=models.IntegerField(null=True,default=1)
    