from django.shortcuts import render
from .models import SubjectFile

def home_page(request):
    return render(request, 'pages/index.html')

def subject_files_page(request, subject):
    # Проверяем, что subject есть в списке допустимых значений
    valid_subjects = [choice[0] for choice in SubjectFile.SUBJECT_CHOICES]
    if subject not in valid_subjects:
        return render(request, 'pages/404.html')  # Страница для ошибки 404
    
    files = SubjectFile.objects.filter(subject=subject)
    context = {
        'files': files,
        'subject_name': dict(SubjectFile.SUBJECT_CHOICES)[subject],  # Название предмета (на русском)
        'subject': subject  # Передаем subject для использования в шаблоне (напр., для изображений)
    }
    return render(request, 'pages/list.html', context)