from django.shortcuts import render, redirect
from .models import Courses

# Create your views here.
def index(request):
    context = {
    "Courses" : Courses.objects.all()
    }
    print "completed index"
    return render(request, "coursesApp/index.html", context)
def create(request):
    print "started create"
    Courses.objects.create(name = request.POST['name'], description = request.POST['description'])
    print "completed create"
    return redirect("/")
def destroy(request, id):
    context = {
    "Course" : Courses.objects.get(id=id)
    }
    return render(request, "coursesApp/destroy.html", context)
def remove(request, id):
    Courses.objects.get(id=id).delete()
    return redirect("/")
