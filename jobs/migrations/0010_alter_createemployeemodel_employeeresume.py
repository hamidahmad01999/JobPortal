# Generated by Django 4.2.4 on 2023-08-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_createemployeemodel_employeeresume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createemployeemodel',
            name='employeeResume',
            field=models.FileField(default='No Resume', upload_to='resume/'),
        ),
    ]