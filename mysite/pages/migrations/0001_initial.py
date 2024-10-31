# Generated by Django 4.2.16 on 2024-10-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('physics', 'Физика'), ('chemistry', 'Химия'), ('biology', 'Биология')], max_length=20, verbose_name='Предмет')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='ZIP файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]