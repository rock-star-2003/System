# Generated by Django 4.2.15 on 2024-08-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_studentadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
