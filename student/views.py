from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *
from django.http import HttpResponse, HttpResponseForbidden

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
        return redirect('student_list')
    return render(request,'students/add-student.html')

def student_list(request):
    student_data = student.objects.select_related('parents').all()
    context = {
        'student_data':student_data
    }
    
    
    return render(request,'students/students.html',context)

def edit_student(request,slug):
    student_details = get_object_or_404(student,slug = slug)
    parents = student_details.parents if hasattr(student_details, 'parents') else None
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
        parents.father_name = request.POST.get('father_name')
        parents.father_occuption=request.POST.get('father_occuption')
        parents.father_mobile = request.POST.get('father_mobile')
        parents.father_email = request.POST.get('father_email')
        parents.mother_name = request.POST.get('mother_name')
        parents.mother_occuption=request.POST.get('mother_occuption')
        parents.mother_mobile = request.POST.get('mother_mobile')
        parents.mother_email = request.POST.get('mother_email')
        parents.present_address = request.POST.get('present_address')
        parents.permanent_address = request.POST.get('permanent_address')
        parents.save()
        
        
        student_details.first_name=first_name
        student_details.last_name=last_name
        student_details.student_id=student_id
        student_details.dob=dob
        student_details.gender=gender
        student_details.student_class=student_class
        student_details.religion=religion
        student_details.joining_date=joining_date
        student_details.mobile_number=mobile_number
        student_details.addmission_number=addmission_number
        student_details.blood_group=blood_group
        student_details.section=section
        student_details.student_image=student_image
        student_details.save()
        create_notification = (request.user,f"{student_details.first_name} {student_details.last_name} has been Updated",student_details)
        
        return redirect('student_list')
    return render(request,'students/edit-student.html',{'student_details':student_details,'parents':parents,})

def view_student(request,slug):
    view_student = get_object_or_404(student, student_id = slug)
    context = {
        'view_student': view_student
    }
    return render(request,'students/student-details.html',context)

def delete_student(request,slug):
    if request.method == 'POST':
        student_delete = get_object_or_404(student, slug = slug)
        student_delete_name = student_delete.first_name
        student_delete.delete()
        create_notification = (request.user,f"{student_delete_name} has been Deleted",student_delete)
        return redirect('student_list')
    return HttpResponseForbidden()
