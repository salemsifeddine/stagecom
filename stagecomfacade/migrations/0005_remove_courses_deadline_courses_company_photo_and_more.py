# Generated by Django 4.0.3 on 2022-06-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stagecomfacade', '0004_courses_remove_course_owner_remove_course_students_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='deadline',
        ),
        migrations.AddField(
            model_name='courses',
            name='company_photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='courses',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
