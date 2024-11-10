from django.db import models

SUBJECT_CHOICES = [
        ('phys', 'Физика'),
        ('chem', 'Химия'),
        ('bio', 'Биология'),
    ]

class SubjectFile(models.Model):
    def __str__(self):
        return f"{self.subject} - {self.file.name}"
    image = models.ImageField(verbose_name='Фото', upload_to='uploads/', null=True)
    subject = models.CharField(max_length=4, choices=SUBJECT_CHOICES, verbose_name="Предмет", null=True)
    file = models.FileField(upload_to='uploads/', verbose_name="ZIP файл", null=True)
    name = models.CharField(verbose_name='Название', max_length=150, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки", null=True)
    description = models.TextField(verbose_name='Описание', null=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"

        
