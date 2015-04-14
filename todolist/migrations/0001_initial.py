# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('todo_job', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 4, 14, 0, 9, 43, 146993), editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=200)),
                ('join_date', models.DateTimeField(default=datetime.datetime(2015, 4, 14, 0, 9, 43, 146490), editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(to='todolist.User'),
        ),
    ]
