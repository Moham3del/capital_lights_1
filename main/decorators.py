from django.shortcuts import redirect


def notLoggedUser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                
                group = request.user.groups.all()[2].name
                
            if group in allowedGroups:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_permission')
        return wrapper_func
    return decorator


# DECORATORS

    def contract_main_index(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name='contract_main_index').exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('no_permission')
        return wrapper_func

