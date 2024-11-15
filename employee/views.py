from django.shortcuts import render

# Create your views here.

from core.decorators import group_required

@group_required('Employee')
def dashboard(request):
    return render(request, 'employee/dashboard.html')
