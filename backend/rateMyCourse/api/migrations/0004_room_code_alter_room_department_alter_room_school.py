# Generated by Django 4.0.3 on 2022-05-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_host_room_course_remove_room_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='code',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='department',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='school',
            field=models.CharField(default='', max_length=50),
        ),
    ]
