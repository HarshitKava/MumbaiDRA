from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.LoginPage,name="Login"),
    path('Logout/', views.LogoutUser,name="Logout"),
    path('Navbar/',views.Navbar,name="Navbar" ),

    #password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),#template_name="LabourReport/password_reset.html"
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),#template_name="LabourReport/password_reset_sent.html"
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),#template_name="LabourReport/password_reset_form.html"
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),#template_name="LabourReport/password_reset_done.html"

    path('Admin/', views.HomeAdmin,name="HomeAdmin"),
    path('AddUser/', views.AddUser,name="AddUser"),
    path('AddArea/', views.AddArea,name="AddArea"),
    path('AddContractor/', views.AddContractor,name="AddContractor"),
    path('AddLabours/', views.AddLabours,name="AddLabours"),
    path('LabourOfContractor/', views.LaboursOfContractor,name="LabourOfContractor"),
    path('ResetPassword/', views.ResetPassword,name="ResetPassword"),
    path('ajax-load-Labour/', views.load_labour,name="ajax_load_labour"),
    path('ajax-load-cat/', views.load_cat,name="ajax_load_cat"),

    path('SE/', views.HomeSE,name="HomeSE"),
    path('AddDaySE/', views.AddDaySE,name="AddDaySE"),
    path('ViewDaySE/', views.ViewDaySE,name="ViewDaySE"),
    path('DeleteSE/<str:i>/', views.DeleteDaySE,name="DeleteSE"),
    path('AddNightSE/', views.AddNightSE,name="AddNightSE"),
    path('ViewNightSE/', views.ViewNightSE,name="ViewNightSE"),
    path('DeleteNightSE/<str:i>', views.DeleteNightSE,name="DeleteNightSE"),
    
    path('HomeSLI/', views.HomeSLI,name="HomeSLI"),
    path('AddDaySLI/', views.AddDaySLI,name="AddDaySLI"),
    path('DeleteDaySLI/<str:i>/<str:A>/<str:N>/<str:C>/<int:L>/<int:H>/', views.DeleteDaySLI,name="DeleteDaySLI"),
    path('AddNightSLI/', views.AddNightSLI,name="AddNightSLI"),
    path('ViewDaySLI/', views.ViewDaySLI,name="ViewDaySLI"),
    path('ViewNightSLI/', views.ViewNightSLI,name="ViewNightSLI"),
    path('DeleteNightSLI/<str:i>/<str:A>/<str:N>/<str:C>/<int:L>/<int:H>/', views.DeleteNightSLI,name="DeleteNightSLI"),
    
    path('HomeCLI/', views.HomeCLI,name="HomeCLI"),
    path('AddDayCLI/', views.AddDayCLI,name="AddDayCLI"),
    path('ViewDayCLI/', views.ViewDayCLI,name="ViewDayCLI"),
    path('DeleteDayCLI/<str:i>/<str:A>/<str:N>/<str:C>/<int:L>/<int:H>/', views.DeleteDayCLI,name="DeleteDayCLI"),
    path('AddNightCLI/', views.AddNightCLI,name="AddNightCLI"),
    path('ViewNightCLI/', views.ViewNightCLI,name="ViewNightCLI"),
    path('DeleteNightCLI/<str:i>/<str:A>/<str:N>/<str:C>/<int:L>/<int:H>/', views.DeleteNightCLI,name="DeleteNightCLI"),

    path('HomeMang/', views.HomeMang,name="HomeMang"),
    path('Export/',views.SiteReport,name="Export"),
    path('FinalReport/',views.FinalReport,name="FinalReport"),
]
