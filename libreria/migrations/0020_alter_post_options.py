# Generated by Django 4.2 on 2023-07-15 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0019_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]