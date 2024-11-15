from django.shortcuts import render

# Create your views here.

from core.decorators import group_required
from core.models import Manager, Answer


@group_required('Manager')
def dashboard(request):
    return render(request, 'manager/dashboard.html')

# manager/views.py

@group_required('Manager')
def view_evaluations(request):
    manager = Manager.objects.get(user=request.user)
    employees = manager.employees.all()
    evaluations = Answer.objects.filter(employee__in=employees)
    return render(request, 'manager/view_evaluations.html', {'evaluations': evaluations})


#cloner174