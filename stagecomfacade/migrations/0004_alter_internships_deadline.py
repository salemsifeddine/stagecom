# Generated by Django 3.2.8 on 2021-12-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagecomfacade', '0003_alter_internships_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internships',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
