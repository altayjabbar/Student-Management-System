from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student


# Create your views here.
def index(request):

    return render(request, "students/index.html", {"students": Student.objects.all()})


def views_student(request, id):
    student = Student.objects.get.all(pk=id)
    return HttpResponseRedirect(reverse("index"))
