from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        student_class = request.POST.get('student_class')
        religion = request.POST.get('religion')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        addmission_number = request.POST.get('addmission_number')
        blood_group = request.POST.get('blood_group')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')
        
        #Reterive Paremts Info
        father_name = request.POST.get('father_name')
        father_occuption=request.POST.get('father_occuption')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occuption=request.POST.get('mother_occuption')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        
        parents_info = parents.objects.create(
            father_name=father_name,
            father_occuption=father_occuption,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_occuption=mother_occuption,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )
        
        student_info = student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            dob=dob,
            gender=gender,
            student_class=student_class,
            religion=religion,
            joining_date=joining_date,
            mobile_number=mobile_number,
            addmission_number=addmission_number,
            blood_group=blood_group,
            section=section,
            student_image=student_image,
            parents=parents_info
        )
        messages.success(request,'Student Added Successfully')
        # return render(request,'students/student_list')
        
        
    return render(request,'students/add-student.html')

def student_list(request):
    return render(request,'students/students.html')

def edit_student(request):
    return render(request,'students/edit-student.html')

def view_student(request):
    return render(request,'students/student-dashboard.html')