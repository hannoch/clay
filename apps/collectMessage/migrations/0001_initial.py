# Generated by Django 2.0.5 on 2019-04-17 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NS', models.CharField(max_length=50, null=True, verbose_name='昵称')),
                ('IP', models.CharField(max_length=30, null=True, verbose_name='ip')),
                ('Title', models.CharField(max_length=50, null=True, verbose_name='域名')),
                ('Server', models.CharField(max_length=50, null=True, verbose_name='服务器')),
                ('Address', models.CharField(default='', max_length=100, null=True, verbose_name='地址')),
                ('GPS', models.CharField(max_length=30, null=True, verbose_name='GPS')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '域名解析',
                'verbose_name_plural': '域名解析',
            },
        ),
    ]
