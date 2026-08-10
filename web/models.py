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
