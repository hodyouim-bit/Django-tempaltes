from django import forms
from .models import student, Subject, Category

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['prefix', 'st_id', 'fname', 'lname', 'mj_id']
        labels = {
            'prefix': 'คำนำหน้าชื่อ',
            'st_id': 'รหัสนักศึกษา',
            'fname': 'ชื่อ',
            'lname': 'นามสกุล',
            'mj_id': 'สาขาวิชา',
        }
        widgets = {
            'prefix': forms.Select(attrs={'class': 'form-select'}),
            'st_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น 64010001'}),
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ระบุชื่อ'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ระบุนามสกุล'}),
            'mj_id': forms.Select(attrs={'class': 'form-select'}),
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_code', 'sub_name', 'category']
        labels = {
            'sub_code': 'รหัสวิชา',
            'sub_name': 'ชื่อรายวิชา',
            'category': 'หมวดหมู่',
        }
        widgets = {
            'sub_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น CS101'}),
            'sub_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น การเขียนโปรแกรมคอมพิวเตอร์ 1'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'ชื่อหมวดหมู่',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น วิชาบังคับ'}),
        }
