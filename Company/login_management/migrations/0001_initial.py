# Generated by Django 5.1 on 2024-11-06 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLogin',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_id', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('employee_name', models.CharField(max_length=100)),
            ],
        ),
    ]
