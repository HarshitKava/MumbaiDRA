from django.urls import path
from . import views
urlpatterns = [
    path('HomeMang/', views.HomeMangProRepo,name="HomeMangProRepo"),

    path('HomeAdmin/', views.HomeAdminProRepo,name="HomeAdminProRepo"),
    path('Activity/', views.Activity,name="AddActivity"),
    path('Structure/', views.AddStructure,name="AddStructure"),
    path('ajax-load-Contractor/', views.ajax_load_Contractor,name="ajax_load_Contractor"),
    path('ajax-load-Category/', views.load_category,name="ajax_load_category"),
    path('ajax_load_LabCat/', views.ajax_load_LabCat,name="ajax_load_LabCat"),

    path('HomeSE/', views.HomeSEProRepo,name="HomeSEProRepo"),
    path('SEAddProRepo/<int:i>/', views.SEAddProRepo,name="SEAddProRepo"),
    path('SEAddProRepo1/', views.SEAddProRepo1,name="SEAddProRepo1"),
    path('SEViewDayProRepo/', views.SEViewDayProRepo,name="SEViewDayProRepo"),
    path('SEDelDayProRepo/<int:i>/', views.SEDelDayProRepo,name="SEDelDayProRepo"),
    path('SEAddNightProRepo/', views.SEAddNightProRepo,name="SEAddNightProRepo"),
    path('SEViewNightProRepo/', views.SEViewNightProRepo,name="SEViewNightProRepo"),
    path('SEDelNightProRepo/<int:i>/', views.SEDelNightProRepo,name="SEDelNightProRepo"),
]