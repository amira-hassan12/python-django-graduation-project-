# Generated by Django 4.0.4 on 2022-05-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=190)),
                ('l_name', models.CharField(max_length=190)),
                ('email', models.CharField(max_length=190, null=True)),
                ('phone', models.CharField(max_length=190, null=True)),
                ('age', models.CharField(max_length=190, null=True)),
            ],
        ),
    ]
