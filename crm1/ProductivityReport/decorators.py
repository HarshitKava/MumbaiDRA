from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user.groups.all()[0].name)
            # return redirect('Login')
            if request.user.groups.all()[0].name == "Admin":
                return redirect('HomeAdmin')
            elif request.user.groups.all()[0].name == "Site Engineer":
                return redirect('HomeSE')
            elif request.user.groups.all()[0].name == "Site Labour Incahrge":
                return redirect('HomeSLI')
            elif request.user.groups.all()[0].name == "Camp Labour Incahrge":
                return redirect('HomeCLI')
            elif request.user.groups.all()[0].name == "Management":
                return redirect('HomeMang')
            else:
                return redirect('Login')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

