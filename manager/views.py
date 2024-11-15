from django.shortcuts import render

# Create your views here.

from core.decorators import group_required

@group_required('Manager')
def dashboard(request):
    return render(request, 'manager/dashboard.html')

#cloner174