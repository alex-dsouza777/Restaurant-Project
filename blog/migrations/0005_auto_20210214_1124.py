# Generated by Django 3.1.5 on 2021-02-14 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
