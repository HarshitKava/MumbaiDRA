from django.shortcuts import render, redirect
from .models import *
from LabourReport.models import *
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, unauthenticated_user
from .forms import *
from datetime import date
from datetime import datetime, timedelta
# Create your views here.

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Management'])
def HomeMangProRepo(request):
    return render(request,'ProductivityReport/Mang/HomeMangProRepo.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admin'])
def HomeAdminProRepo(request):
    return render(request,'ProductivityReport/Admin/HomeAdminProRepo.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admin'])
def Activity(request):
    Form=CategoryOfDeploymentForm()
    data = CategoryOfDeployment.objects.all()
    if request.method=='POST':
        Form=CategoryOfDeploymentForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('AddActivity')
    return render(request,'ProductivityReport/Admin/Activity.html',{'Form':Form,'data':data})

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Admin'])
def AddStructure(request):
    Form=StructureForm()
    data = Structure.objects.all()
    if request.method=='POST':
        Form=StructureForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('ShowStructure')
    return render(request,'ProductivityReport/Admin/Structure.html',{'Form':Form,'data':data})


@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def HomeSEProRepo(request):
    return render(request,'ProductivityReport/SE/HomeSEProRepo.html')

@login_required(login_url='Login')
@allowed_users(allowed_roles=['Site Engineer'])
def SEAddProRepo(request,i):

    Form=ProductivityReportForm()
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    if Areaname:
        Areaname_id=Areaname[0].id
        Areaname = Areaname[0].AreaName
    today = datetime.now()
    tomorrow = today + timedelta(1)
    d2=tomorrow.strftime("%Y-%m-%d")
    d1 = today.strftime("%Y-%m-%d")
    # print("type(d".id),d1,d2)
    Report=SiteEngDay.objects.filter(id=i)
    # print(request.method)
    Form=ProductivityReportForm()
    if request.method=='POST':
        Form=ProductivityReportForm(request.POST)
        # find error in Form
        # fill the empty fields
        print(request.POST)
        new_data=request.POST.copy()
        if Form.errors:
            new_data=request.POST.copy()
            for i in Form.errors:
                new_data[i]="1"
        Form=ProductivityReportForm(new_data)
        if Form.is_valid():
            if ProductivityReport.objects.filter(LRid=request.POST['LRid']):
                data=ProductivityReport.objects.filter(LRid=request.POST['LRid'])
                data.delete()
            Form.save()
        return redirect('SEAddProRepo1')
    return render(request,'ProductivityReport/SE/SEAddDayProRepo.html',{'Form':Form,'Report':Report,'Areaname':Areaname,'Areaname_id':Areaname_id,'d1':d1,'d2':d2})

@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def SEAddProRepo1(request):
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    Areaname_id=Areaname[0].id
    Areaname = Areaname[0].AreaName
    today = datetime.now()
    tomorrow = today + timedelta(1)
    d2=tomorrow.strftime("%Y-%m-%d")
    d1 = today.strftime("%Y-%m-%d")
    # print("d",d1,d2)
    ProReport=ProductivityReport.objects.filter()
    LRids=ProductivityReport.objects.filter().values('LRid').distinct()
    LRids=list(LRids)
    LRids=[i['LRid'] for i in LRids]
    print(LRids)
    # print(ProReport)
    Report=SiteEngDay.objects.filter(created_at__range=[d1,d2],Areaname=Areaname_id)
    return render(request,'ProductivityReport/SE/SEAddDayProRepo_1.html',{'LRids':LRids,'ProReport':ProReport,'Report':Report,'Areaname':Areaname,'Areaname_id':Areaname_id,'d1':d1,'d2':d2})

@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def SEViewDayProRepo(request):
    today = datetime.now()
    today = today + timedelta(1)
    tomorrow = today - timedelta(5)
    d2=tomorrow.strftime("%Y-%m-%d")
    d1 = today.strftime("%Y-%m-%d")
    print(d1,d2)
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    Areaname_id=Areaname[0].id
    Report=ProductivityReport.objects.filter(Areaname=Areaname_id,created_at__range=[d2,d1])
    return render(request,'ProductivityReport/SE/SEViewDayProRepo.html',{'Report':Report,'Areaname':Areaname,'Areaname_id':Areaname_id})

@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def SEDelDayProRepo(request,i):
    data=ProductivityReport.objects.get(id=i)
    data.delete()
    return redirect('SEAddProRepo')

@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def SEDelNightProRepo(request,i):
    data=ProductivityNightReport.objects.get(id=i)
    data.delete()
    return redirect('SEAddNightProRepo')

@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def SEViewNightProRepo(request):
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    Areaname_id=Areaname[0].id
    Report=ProductivityNightReport.objects.filter(Areaname=Areaname_id)
    return render(request,'ProductivityReport/SE/SEViewNightProRepo.html',{'Report':Report,'Areaname':Areaname,'Areaname_id':Areaname_id})

@login_required(login_url='Login')
@allowed_users(allowed_roles=[''])
def SEAddNightProRepo(request):
    Form=ProductivityNightReportForm()
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    Areaname_id=Areaname[0].id
    Areaname = Areaname[0].AreaName
    today = datetime.now()
    tomorrow = today + timedelta(1)
    d2=tomorrow.strftime("%Y-%m-%d")
    d1 = today.strftime("%Y-%m-%d")
    # print("d",d1,d2)
    Report=ProductivityNightReport.objects.filter(Areaname=Areaname_id,created_at__range=[d1,d2])
    if request.method=='POST':
        Form=ProductivityNightReportForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('SEAddNightProRepo')
    return render(request,'ProductivityReport/SE/SEAddNightProRepo.html',{'Form':Form,'Report':Report,'Areaname':Areaname,'Areaname_id':Areaname_id,'d1':d1,'d2':d2})

@login_required(login_url='Login')
# @allowed_users(allowed_roles=['Site Engineer'])
def ajax_load_Contractor(request):
    today = datetime.now()
    tomorrow = today + timedelta(1)
    d2=tomorrow.strftime("%Y-%m-%d")
    d1 = today.strftime("%Y-%m-%d")
    # get user area
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    Area_id=Areaname[0].id
    Areaname = Areaname[0].AreaName
    Structure_id = request.GET.get('contractor_id')
    print(Structure_id)
    Contractor = SiteEngDay.objects.filter(Areaname_id=Area_id,StructureName_id=Structure_id,created_at__range=[d1,d2]).distinct()
    print(Contractor,Contractor[0].ContractorName)
    return render(request, 'ProductivityReport/contractor_list_options.html', {'data': Contractor})

@login_required(login_url='Login')
# @allowed_users(allowed_roles=['Site Engineer'])
def ajax_load_LabCat(request):
    today = datetime.now()
    tomorrow = today + timedelta(1)
    d2=tomorrow.strftime("%Y-%m-%d")
    d1 = today.strftime("%Y-%m-%d")
    # get user area
    current_user = request.user
    Areaname = Area.objects.filter(Username=current_user.username)
    Area_id=Areaname[0].id
    Areaname = Areaname[0].AreaName
    Contractor_id = request.GET.get('contractor_id')
    Structure_id = request.GET.get('structure_id')
    print(Contractor_id,Structure_id)
    return render(request, 'ProductivityReport/labcat_list_options.html')#, {'data': Contractor})


@login_required(login_url='Login')
# @allowed_users(allowed_roles=['Site Engineer'])
def load_category(request):
    activity_id = request.GET.get('activity_id')
    print("activity_id",activity_id)


    for i in AddLabour.objects.filter(id=int(activity_id)):
        print(i.id,i)
    activity_name2=AddLabour.objects.get(id=int(activity_id))
    print("activity_name2",activity_name2,activity_name2.id)


    for i in CategoryOfDeployment.objects.all():

        print(i.id,i.ActivityName,i.CategoryName)
    # filter by activity name
    Category = CategoryOfDeployment.objects.filter(ActivityName=activity_name2)
    # print( CategoryOfDeployment.objects.filter(ActivityName=activity_id))
    # Category=""
    print("Category",Category)
    #CategoryOfDeployment.objects.filter(ActivityName=Category.id)
    return render(request, 'LabourReport/Admin/category_dropdown_list_options.html', {'Category': Category})
