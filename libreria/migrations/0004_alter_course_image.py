# Generated by Django 4.2 on 2023-06-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_course_description_alter_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Course Image'),
        ),
    ]
