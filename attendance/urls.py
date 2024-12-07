from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_attendance, name='attendance_register'),
    path('success/', views.attendance_success, name='attendance_success'),
    path('calendar/', views.calendar_view, name='calendar'),
]
