from django.db import models

class SubjectFile(models.Model):
    SUBJECT_CHOICES = [
        ('physics', 'Физика'),
        ('chemistry', 'Химия'),
        ('biology', 'Биология'),
    ]

    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, verbose_name="Предмет")
    file = models.FileField(upload_to='uploads/', verbose_name="ZIP файл")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")

    def __str__(self):
        return f"{self.subject} - {self.file.name}"

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
