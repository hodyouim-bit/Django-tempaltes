from django import forms
from .models import student

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
            'st_id': forms.TextInput(attrs={'class': 'form-control-lg', 'placeholder': 'เช่น 64010001'}),
            'fname': forms.TextInput(attrs={'class': 'form-control-lg', 'placeholder': 'ระบุชื่อ'}),
            'lname': forms.TextInput(attrs={'class': 'form-control-lg', 'placeholder': 'ระบุนามสกุล'}),
            'mj_id': forms.Select(attrs={'class': 'form-select'}),
        }
