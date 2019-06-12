from django import forms
from onlineapp.models import Student,MockTest1


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'dropped_out', 'college']

class Marks(forms.ModelForm):
    class Meta:
        model = MockTest1
        exclude = ['id', 'student', 'total']