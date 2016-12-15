# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161116_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='part1',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part10',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part11',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part2',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part3',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part4',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part5',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part6',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part7',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part8',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='part9',
            field=models.CharField(blank=True, default=b'', max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty1',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty10',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty11',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty2',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty4',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty5',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty6',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty7',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty8',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
        migrations.AddField(
            model_name='container',
            name='qty9',
            field=models.IntegerField(blank=True, default=b'', null=True),
        ),
    ]
