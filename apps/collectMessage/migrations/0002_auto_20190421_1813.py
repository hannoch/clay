# Generated by Django 2.0.5 on 2019-04-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectMessage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='Address',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='GPS',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='GPS'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='IP',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ip'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='NS',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='域名'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='Server',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='服务器'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='Title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='标题'),
        ),
    ]
