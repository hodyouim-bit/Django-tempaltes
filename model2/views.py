import datetime
from functools import wraps
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from web.models import student, Subject, Category
from web.forms import StudentForm, SubjectForm, CategoryForm, UserLoginForm, UserRegisterForm


def admin_required(view_func):
    @wraps(view_func)
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            raise PermissionDenied("สำหรับแอดมินเท่านั้น (Admin Only)")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get("next", "home")
            return redirect(next_url)
    else:
        form = UserLoginForm()

    context = {
        "title": "เข้าสู่ระบบ (Login)",
        "form": form,
        "date": datetime.date.today(),
    }
    return render(request, "registration/login.html", context)


def user_register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()

    context = {
        "title": "สมัครสมาชิก (Sign Up / Register)",
        "form": form,
        "date": datetime.date.today(),
    }
    return render(request, "registration/register.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


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


@admin_required
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


@admin_required
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


@admin_required
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


# Subject Views
def subject_list(request):
    subjects = Subject.objects.select_related("category").all().order_by("id")
    context = {
        "title": "รายชื่อวิชา",
        "date": datetime.date.today(),
        "subjects": subjects,
    }
    return render(request, "subject_list.html", context)


def subject_detail(request, pk):
    sub = get_object_or_404(Subject, pk=pk)
    context = {
        "title": "รายละเอียดวิชา",
        "date": datetime.date.today(),
        "subject": sub,
    }
    return render(request, "subject_detail.html", context)


@admin_required
def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            new_sub = form.save()
            return redirect("subject_detail", pk=new_sub.pk)
    else:
        form = SubjectForm()

    context = {
        "title": "เพิ่มข้อมูลวิชา",
        "form": form,
        "is_edit": False,
        "date": datetime.date.today(),
    }
    return render(request, "subject_form.html", context)


@admin_required
def subject_update(request, pk):
    sub = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=sub)
        if form.is_valid():
            form.save()
            return redirect("subject_detail", pk=sub.pk)
    else:
        form = SubjectForm(instance=sub)

    context = {
        "title": "แก้ไขข้อมูลวิชา",
        "form": form,
        "subject": sub,
        "is_edit": True,
        "date": datetime.date.today(),
    }
    return render(request, "subject_form.html", context)


@admin_required
def subject_delete(request, pk):
    sub = get_object_or_404(Subject, pk=pk)
    if request.method == "POST":
        sub.delete()
        return redirect("subject_list")

    context = {
        "title": "ลบข้อมูลวิชา",
        "subject": sub,
        "date": datetime.date.today(),
    }
    return render(request, "subject_confirm_delete.html", context)