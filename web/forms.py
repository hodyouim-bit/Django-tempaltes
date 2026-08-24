from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
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


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="ชื่อผู้ใช้ (Username)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ระบุชื่อผู้ใช้'})
    )
    password = forms.CharField(
        label="รหัสผ่าน (Password)",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'ระบุรหัสผ่าน'})
    )


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="ชื่อจริง (First Name)",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ระบุชื่อจริง'})
    )
    last_name = forms.CharField(
        label="นามสกุล (Last Name)",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ระบุนามสกุล'})
    )
    email = forms.EmailField(
        label="อีเมล (Email)",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'เช่น name@example.com'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'ชื่อผู้ใช้ (Username)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if name == 'username':
                field.widget.attrs['placeholder'] = 'ตั้งชื่อผู้ใช้สำหรับเข้าสู่ระบบ'


