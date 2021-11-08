from django import forms


class CourseSearch(forms.Form):
    course_title = forms.CharField()
    category = forms.Select()

