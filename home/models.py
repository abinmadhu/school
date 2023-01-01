from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=200)


    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=200)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Purpose(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Detail(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField(null=False)
    age=models.IntegerField()
    gender_is_male=models.BooleanField("Male",default=False,null=True)
    gender_is_female=models.BooleanField("Female",default=False,null=True)
    number=models.IntegerField()
    email=models.EmailField(null=True)
    address=models.TextField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    purpose=models.ForeignKey(Purpose,on_delete=models.CASCADE)
    material_book=models.BooleanField("Note Book",default=False,null=True)
    material_pen=models.BooleanField("Pen",default=False,null=True)
    material_paper=models.BooleanField("Exam Paper",default=False,null=True)

    def __str__(self):
        return self.name
