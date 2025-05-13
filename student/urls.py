from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('student-list/', views.student_list, name='student_list'),
    path('view-student<str:slug>/', views.view_student, name='view_student'),
    path('edit-student/<str:slug>/', views.edit_student, name='edit_student'),
    path('delete-student/<str:slug>/', views.delete_student, name='delete_student'),
]
