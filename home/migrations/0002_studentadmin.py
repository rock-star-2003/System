# Generated by Django 4.2.15 on 2024-08-29 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('joined_date', models.DateField(blank=True, null=True)),
                ('select_bach', models.CharField(blank=True, max_length=2, null=True)),
                ('bach_time', models.DateField(blank=True, null=True)),
                ('fees', models.CharField(blank=True, max_length=10, null=True)),
                ('attendence', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
