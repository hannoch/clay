# Generated by Django 2.0.5 on 2019-04-21 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=11, null=True, verbose_name='电话'),
        ),
    ]
