from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json

from main.models import Submission

# Create your views here.
def home(request):
    submissions = Submission.objects.all().order_by("-time_submitted")
    return render(request, 'main/index.html', context={"submissions": submissions})


def submission(request, submission_id):
    try:
        submission = Submission.objects.get(pk=submission_id)
    except Submission.DoesNotExist:
        return Http404("Submission does not exist")
    
    return render(request, "main/detail.html", context={"submission": submission})


def student_detail(request, student_name):
    submissions = Submission.objects.filter(student_name=student_name).order_by("assignment_name", "-time_submitted")
    if not submissions:
        return Http404(f"Student {student_name} does not exist")
    student = {
        "name": submissions[0].student_name,
        "email": submissions[0].student_email,
    }
    return render(request, "students/detail.html", context={"student": student, "submissions": submissions})


def classroom_detail(request, classroom_name):
    students = Submission.objects.filter(classroom_name=classroom_name).values_list("student_name", flat=True).distinct()
    if not students:
        return Http404(f"Classroom {classroom_name} does not exist")

    return render(request, "classrooms/detail.html", context={"students": students})

# TODO: create student view

@csrf_exempt
def submit(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Submission.parse_from_webhook_data(data)

    return HttpResponse()


def create_fixtures(request):
    submissions = Submission.generate_fixtures()
    return render(request, 'main/fixture_view.html', context={"submissions": submissions})


def clear_all_data():
    Submission.all().delete()
