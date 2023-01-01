from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Detail,Course

class RegForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# widget=forms.CheckboxInput(attrs={'placeholder':'Female','required':'False'})
class DetailForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter yoyr name'}))
    dob=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email id'}))
    number=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter your Phone number'}))
    gender_is_male=forms.BooleanField(required=False)
    gender_is_female=forms.BooleanField(required=False)
    material_book=forms.BooleanField(required=False)
    material_pen=forms.BooleanField(required=False)
    material_paper=forms.BooleanField(required=False)
    address=forms.Textarea()
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter yoyr age'}))
    class Meta:
        model= Detail
        fields="__all__"

    def __init__(self,*args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields['course'].queryset=Course.objects.none()

          if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
          elif self.instance.pk:
            self.fields['course'].queryset=self.instance.department.course_set.order_by('name')  
          
