# Generated by Django 3.2.8 on 2021-12-15 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stagecomfacade', '0004_alter_internships_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internships',
            name='deadline',
        ),
    ]
