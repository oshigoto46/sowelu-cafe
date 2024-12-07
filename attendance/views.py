from django.shortcuts import render, redirect
from datetime import date
import calendar
from .models import Attendance
from .forms import AttendanceForm

def register_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_success')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/register.html', {'form': form})

def attendance_success(request):
    return render(request, 'attendance/success.html')

def calendar_view(request):
    # 現在の月
    today = date.today()
    year = request.GET.get('year', today.year)
    month = request.GET.get('month', today.month)

    # 勤務情報を取得
    attendance_data = Attendance.objects.filter(date__year=year, date__month=month)

    # 勤務者情報を辞書に整理
    attendance_dict = {}
    for attendance in attendance_data:
        if attendance.date.day not in attendance_dict:
            attendance_dict[attendance.date.day] = []
        attendance_dict[attendance.date.day].append(attendance.name)

    # カレンダーを作成
    cal = calendar.Calendar(firstweekday=0)  # 月曜日開始
    days = cal.itermonthdays(int(year), int(month))

    context = {
        'year': year,
        'month': month,
        'days': days,
        'attendance_dict': attendance_dict,
        'month_name': calendar.month_name[int(month)],
    }

    return render(request, 'attendance/calendar.html', context)
