# Generated by Django 4.2.7 on 2023-11-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_course_options_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='addres',
            new_name='address',
        ),
    ]
