from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


class CustomLoginView(auth_views.LoginView):
    template_name = 'core/login.html'
    


@login_required
def redirect_view(request):
    if request.user.groups.filter(name='Senior Manager').exists():
        return redirect('senior_manager:dashboard')
    elif request.user.groups.filter(name='Manager').exists():
        return redirect('manager:dashboard')
    elif request.user.groups.filter(name='Employee').exists():
        return redirect('employee:dashboard')
    else:
        return redirect('login')

#cloner174