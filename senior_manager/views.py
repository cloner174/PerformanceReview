from django.shortcuts import render

# Create your views here.

from core.decorators import group_required

@group_required('Senior Manager')
def dashboard(request):
    return render(request, 'senior_manager/dashboard.html')

#cloner174