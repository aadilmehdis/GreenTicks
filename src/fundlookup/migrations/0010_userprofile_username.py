# Generated by Django 2.2 on 2020-02-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundlookup', '0009_userprofile_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='', max_length=120, verbose_name='Name'),
        ),
    ]