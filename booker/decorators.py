from django.http import HttpResponse
from django.shortcuts import redirect


# it added to the file by using @unauthenticated_user
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenthicated:
            return redirect('subroute_home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# added like allowed 34r|\|44|\| @allowed_users(allowed_roles=['admin','me'])
def allowed_users(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = 'booker'
        if request.user.role == role:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('you are not authorized ')

    return wrapper_func


def booker_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        role = 'booker'
        if request.user.role == role:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('you are not authorized ')

    return wrapper_func
