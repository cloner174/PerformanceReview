from django.shortcuts import render

# Create your views here.

from core.decorators import group_required
from django.contrib.auth.decorators import login_required
from core.models import Employee
from .forms import EvaluationForm
from core.models import Question, Answer
from django.shortcuts import redirect


@group_required('Employee')
def dashboard(request):
    employee = Employee.objects.get(user=request.user)
    return render(request, 'employee/dashboard.html', {'employee': employee})

# employee/views.py

@group_required('Employee')
def submit_evaluation(request):
    employee = Employee.objects.get(user=request.user)
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            for field_name, value in form.cleaned_data.items():
                question_id = int(field_name.split('_')[1])
                question = Question.objects.get(id=question_id)
                Answer.objects.create(
                    question=question,
                    employee=employee,
                    response=value
                )
            return redirect('employee:dashboard')
    else:
        form = EvaluationForm()
    return render(request, 'employee/submit_evaluation.html', {'form': form})


#cloner174