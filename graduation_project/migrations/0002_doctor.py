# Generated by Django 4.0.4 on 2022-05-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=190)),
                ('l_name', models.CharField(max_length=190)),
                ('address', models.CharField(max_length=190, null=True)),
                ('email', models.CharField(max_length=190, null=True)),
                ('phone', models.CharField(max_length=190, null=True)),
                ('age', models.CharField(max_length=190, null=True)),
            ],
        ),
    ]
