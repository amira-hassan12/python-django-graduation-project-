# Generated by Django 4.0.4 on 2022-05-27 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation_project', '0004_login_signup_doctor_signup_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=190, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='signup_doctor',
            name='age',
        ),
        migrations.RemoveField(
            model_name='signup_doctor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='signup_patient',
            name='address',
        ),
        migrations.RemoveField(
            model_name='signup_patient',
            name='phone',
        ),
    ]