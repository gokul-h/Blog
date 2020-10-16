# Generated by Django 3.1.2 on 2020-10-09 12:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myblog', '0007_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
