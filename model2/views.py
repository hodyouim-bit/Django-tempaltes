import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from web.models import student
from web.forms import StudentForm


def index(request):
    context = {
        "title": "รายชื่อนักศึกษา",
        "date": datetime.date.today(),
        "students": student.objects.all().order_by("id"),
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def Student_detail(request, pk):
    std = get_object_or_404(student, pk=pk)
    context = {
        "title": "รายละเอียดนักศึกษา",
        "date": datetime.date.today(),
        "student": std,
    }
    return render(request, "student_datail.html", context)


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return redirect("Student_detail", pk=new_student.pk)
    else:
        form = StudentForm()

    context = {
        "title": "เพิ่มข้อมูลนักศึกษา",
        "form": form,
        "is_edit": False,
        "date": datetime.date.today(),
    }
    return render(request, "student_form.html", context)


def student_update(request, pk):
    std = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=std)
        if form.is_valid():
            form.save()
            return redirect("Student_detail", pk=std.pk)
    else:
        form = StudentForm(instance=std)

    context = {
        "title": "แก้ไขข้อมูลนักศึกษา",
        "form": form,
        "student": std,
        "is_edit": True,
        "date": datetime.date.today(),
    }
    return render(request, "student_form.html", context)


def student_delete(request, pk):
    std = get_object_or_404(student, pk=pk)
    if request.method == "POST":
        std.delete()
        return redirect("home")

    context = {
        "title": "ลบข้อมูลนักศึกษา",
        "student": std,
        "date": datetime.date.today(),
    }
    return render(request, "student_confirm_delete.html", context)


