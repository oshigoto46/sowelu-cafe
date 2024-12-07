from django.db import models

class Attendance(models.Model):
    name = models.CharField(max_length=100, verbose_name="氏名")  # 氏名
    date = models.DateField(verbose_name="勤務日")  # 勤務日
    start_time = models.TimeField(verbose_name="出勤時間")  # 出勤時間
    end_time = models.TimeField(verbose_name="退勤時間")  # 退勤時間
    remarks = models.TextField(verbose_name="備考", blank=True, null=True)  # 備考

    def __str__(self):
        return f"{self.name} - {self.date}"
