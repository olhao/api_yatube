# Generated by Django 2.2.16 on 2021-10-08 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_commentpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentPost',
        ),
    ]
