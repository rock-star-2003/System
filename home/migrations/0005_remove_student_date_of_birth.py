# Generated by Django 4.2.15 on 2024-08-29 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_student_age_student_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_of_birth',
        ),
    ]
