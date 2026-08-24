from django.db.models import base
from django.db import models
from django.urls import reverse

# Create your models here.
# st_id , fname , lname ,

prefix_NAME = (
    ("นาย", "นาย"),
    ("นางสาว", "นางสาว"),
    ("นาง", "นาง"),
)


class Major(models.Model):
    mj_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.mj_name

class student(models.Model):

    prefix = models.CharField(max_length=100, choices=prefix_NAME, default="นาย")
    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)
    mj_id = models.ForeignKey(Major, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.prefix +"  "+ self.fname + "  " + self.lname

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="หมวดหมู่")

    def __str__(self):
        return self.name


class Subject(models.Model):
    sub_code = models.CharField(max_length=20, unique=True, blank=False, verbose_name="รหัสวิชา")
    sub_name = models.CharField(max_length=200, blank=False, verbose_name="ชื่อวิชา")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="หมวดหมู่")

    def __str__(self):
        return f"{self.sub_code} - {self.sub_name}"

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})

