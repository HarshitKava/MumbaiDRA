from email.policy import default
from django.db import models
from django import forms
from django.conf import settings
from numpy import place

# Create your models here.



class Structure(models.Model):
    StructureName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.StructureName
    
class WorkArea(models.Model):
    WorkAreaName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.WorkAreaName

class Area(models.Model):
    Username=models.CharField(max_length=200, null=True) #ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    # AreaName=models.CharField(max_length=200, null=True,choices=AreaName,default='None')
    AreaName=models.ForeignKey(WorkArea, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.AreaName
    

class ContractorDetail(models.Model):
    ContractorName=models.CharField(max_length=200, null=True)
    ContractorNumber=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class AddLabour(models.Model):
    LabourCategory=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.LabourCategory


class LabourOfContractor(models.Model):
    ContractorName=models.ForeignKey(ContractorDetail, on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('AddLabour', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.LabourCategory)

class CategoryOfDeployment(models.Model):
    ActivityName=models.ForeignKey(AddLabour,on_delete=models.CASCADE,null=True)
    CategoryName=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.CategoryName

class SiteEngDay (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    StructureName=models.ForeignKey('Structure', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class SiteEngNight (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    StructureName=models.ForeignKey(Structure,on_delete=models.CASCADE,null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class SLIDay (models.Model):
    AreaName=[
        ('','None'),
        ('SBN','SBN'),
        ('KV','KV'),
        ('DBM','DBM'),
        ('MPZ','MPZ'),
        ('RKP','RKP'),
        ('HBM','HBM'),
        ('ALK','ALK'),
        ('AIIMS','AIIMS'),
        ('Bangalore','Bangalore'),
        ('Casting Yard','Casting Yard'),
        ('Casting Yard QC','Casting Yard QC'),
        ('Casting Yard PM','Casting Yard PM'),   
    ]
    # Areaname=models.CharField(max_length=200, null=True,choices=AreaName,default='None')
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class SLINight (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True) 
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class CLIDay (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    StructureName=models.ForeignKey('Structure', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

class CLINight (models.Model):
    Areaname=models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True,null=True)
    ContractorName=models.ForeignKey('ContractorDetail', on_delete=models.CASCADE, null=True)
    LabourCategory=models.ForeignKey('LabourOfContractor', on_delete=models.CASCADE, null=True)
    CategoryName=models.ForeignKey(CategoryOfDeployment,on_delete=models.CASCADE,null=True)
    StructureName=models.ForeignKey('Structure', on_delete=models.CASCADE, null=True)
    NoLabor=models.IntegerField(null=True)
    def __str__(self):
        return str(self.ContractorName)

         
# class RFI(models.Model):
#     # Month	Date of Creation	Location	Pier ID	Structure	Discipline	Work	Description of Works	RFI		Date of Inspection	"Time of
# # Inspection"	Contractor's Responsible Person 		Mobile No	Designation	Inspection Conducted by GC	
# 								# No.	Revision
#     # 
#     RFI_Month = models.DateField(null=True)
#     RFI_Name = models.CharField(max_length=200, null=True)
#     RFI_Number = models.IntegerField(null=True)
#     RFI_Image = models.ImageField(null=True, blank=True, upload_to="images/")

#     def __str__(self):
#         return self.RFI_Name

class Report_Status(models.Model):
    Area = models.CharField(max_length=200, null=True)
    Date = models.DateField(null=True)
    Status_Day = models.BooleanField(default=False)
    Status_Night = models.BooleanField(default=False)
    def __str__(self):
        name = self.Area + " " + str(self.Date) + " "

        if self.Status_Day == True:
            name += "(Day : True)" + " "
        else:
            name += "(Day : False)" + " "
        if self.Status_Night == True:
            name += "(Night : True)"
        else:
            name += "(Night : False)"
        
        return name
