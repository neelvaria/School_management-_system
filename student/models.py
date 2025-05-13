from django.db import models
from slugify import slugify

# Create your models here.
class parents(models.Model):
    father_name = models.CharField(max_length=20)
    father_occuption = models.CharField(max_length=20)
    father_mobile = models.BigIntegerField()
    father_email = models.EmailField()
    mother_name = models.CharField(max_length=20)
    mother_occuption = models.CharField(max_length=20)
    mother_mobile = models.BigIntegerField()
    mother_email = models.EmailField()
    present_address = models.TextField()
    permanent_address = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.father_name} & {self.mother_name}"
    
class student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=(('male','male'),('female','female'),('other','other')))
    student_class = models.CharField(max_length=20)
    religion = models.CharField(max_length=20,choices=(('hindu','hindu'),('christian','christian'),('others','others')))
    joining_date = models.DateField()
    mobile_number = models.BigIntegerField()
    addmission_number = models.IntegerField()
    blood_group = models.CharField(max_length=20, choices=(('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')))
    section = models.CharField(max_length=20, choices=(('A','A'),('B','B'),('C','C'),('D','D')))
    student_image = models.ImageField(upload_to="student_image")
    parents = models.ForeignKey(parents, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super(student, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.student_id})"