# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('subsystem', models.CharField(max_length=50)),
                ('supervisor_1', models.CharField(max_length=50)),
                ('supervisor_2', models.CharField(max_length=50)),
                ('supervisor_3', models.CharField(max_length=50)),
                ('respector', models.CharField(max_length=50)),
                ('experiment', models.CharField(max_length=50)),
                ('IP', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('work', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=50)),
                ('stateOrDate', models.CharField(max_length=255)),
                ('More', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Biz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column', models.CharField(max_length=100)),
                ('playStart', models.DateField()),
                ('playFinish', models.DateField()),
                ('numOfNeeds', models.IntegerField()),
                ('allReadyTime', models.DateField()),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('event', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('system', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='system_id',
            field=models.ForeignKey(to='model.System'),
        ),
        migrations.AddField(
            model_name='biz',
            name='system_id',
            field=models.ForeignKey(to='model.System'),
        ),
        migrations.AddField(
            model_name='base',
            name='system_id',
            field=models.ForeignKey(to='model.System'),
        ),
    ]
