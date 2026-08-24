from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("signup/", views.user_register, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("web/", include("web.url")),
    path("student/create/", views.student_create, name="student_create"),
    path("student/<int:pk>/", views.Student_detail, name="Student_detail"),
    path("student/<int:pk>/edit/", views.student_update, name="student_update"),
    path("student/<int:pk>/delete/", views.student_delete, name="student_delete"),
    path("subject/", views.subject_list, name="subject_list"),
    path("subject/create/", views.subject_create, name="subject_create"),
    path("subject/<int:pk>/", views.subject_detail, name="subject_detail"),
    path("subject/<int:pk>/edit/", views.subject_update, name="subject_update"),
    path("subject/<int:pk>/delete/", views.subject_delete, name="subject_delete"),
]
