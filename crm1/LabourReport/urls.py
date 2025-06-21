from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.LoginPage,name="Login"),
    path('Logout/', views.LogoutUser,name="Logout"),
    path('Navbar/',views.Navbar,name="Navbar" ),

    #password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="LabourReport/Reset_Password.html"), name="reset_password"),#template_name="LabourReport/password_reset.html"
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),#template_name="LabourReport/password_reset_sent.html"
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),#template_name="LabourReport/password_reset_form.html"
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),#template_name="LabourReport/password_reset_done.html"

    path('Admin/', views.HomeAdmin,name="HomeAdmin"),
    path('AddUser/', views.AddUser,name="AddUser"),
    path('EditUser/<i>/', views.EditUser,name="EditUser"),
    path('DeleteUser/<i>/', views.DeleteUser,name="DeleteUser"),
    path('AddContractor/', views.AddContractor,name="AddContractor"),
    path('EditContractor/<i>/', views.EditContractor,name="EditContractor"),
    path('DeleteContractor/<i>/', views.DeleteContractor,name="DeleteContractor"),
    path('ShowStructure/', views.ShowStructure,name="ShowStructure"),
    path('EditStructure/<i>/', views.EditStructure,name="EditStructure"),
    path('DeleteStructure/<i>/', views.DeleteStructure,name="DeleteStructure"),
    path('AddLabours/', views.AddLabours,name="AddLabours"),
    path('ShowLabours/', views.ShowLabours,name="ShowLabours"),
    path('EditLabours/<i>/', views.EditLabours,name="EditLabours"),
    path('DeleteLabours/<i>/', views.DeleteLabours,name="DeleteLabours"),
    path('LabourOfContractor/', views.LaboursOfContractor,name="LabourOfContractor"),
    path('ShowLabourOfContractor/', views.ShowLabourOfContractor,name="ShowLabourOfContractor"),
    path('EditLabourOfContractor/<i>/', views.EditLabourOfContractor,name="EditLabourOfContractor"),
    path('DeleteLabourOfContractor/<i>/', views.DeleteLabourOfContractor,name="DeleteLabourOfContractor"),
    path('ShowActivity/', views.ShowActivity,name="ShowActivity"),
    path('EditActivity/<i>/', views.EditActivity,name="EditActivity"),
    path('DeleteActivity/<i>/', views.DeleteActivity,name="DeleteActivity"),
    path('ResetPassword/', views.ResetPassword,name="ResetPassword"),
    path('ajax-load-Labour/', views.load_labour,name="ajax_load_labour"),
    path('ajax-load-cat/', views.load_cat,name="ajax_load_cat"),
    path('Contractor/', views.ShowContractor,name="Contractor"),

    path('SE/', views.HomeSE,name="HomeSE"),
    path('AddDaySE/', views.AddDaySE,name="AddDaySE"),
    path('ViewDaySE/', views.ViewDaySE,name="ViewDaySE"),
    path('EditSE/<i>/', views.EditDaySE,name="EditSE"),
    path('DeleteSE/<str:i>/', views.DeleteDaySE,name="DeleteSE"),
    path('AddNightSE/', views.AddNightSE,name="AddNightSE"),
    path('ViewNightSE/', views.ViewNightSE,name="ViewNightSE"),
    path('DeleteNightSE/<str:i>', views.DeleteNightSE,name="DeleteNightSE"),
    path('DLRSummary/', views.DLRSummary,name="DLRSummary"),
    path('ReportStatus/<str:shift>', views.Change_Report_Status,name="ReportStatus"),
    
    path('HomeSLI/', views.HomeSLI,name="HomeSLI"),
    path('AddDaySLI/', views.AddDaySLI,name="AddDaySLI"),
    path('DeleteDaySLI/<str:i>/', views.DeleteDaySLI,name="DeleteDaySLI"),
    path('AddNightSLI/', views.AddNightSLI,name="AddNightSLI"),
    path('ViewDaySLI/', views.ViewDaySLI,name="ViewDaySLI"),
    path('ViewNightSLI/', views.ViewNightSLI,name="ViewNightSLI"),
    path('DeleteNightSLI/<str:i>/', views.DeleteNightSLI,name="DeleteNightSLI"),
    
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
    path('Dashboard/',views.ManagerDashboard,name="Dashboard"),
    path('LabourRequest/',views.LabourRequest,name="LabourRequest"),
    # path('RFI/',views.RFI,name="RFI"),
    path('SendMail/<str:shift>',views.Send_Emails,name="Send_Emails"),
]
