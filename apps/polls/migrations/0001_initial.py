# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1024)),
                ('value', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_value', models.FloatField()),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PossiblePollResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('image', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=2048)),
                ('name', models.CharField(max_length=256)),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=1024)),
                ('multipe_choice', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='poll',
            name='questions',
            field=models.ManyToManyField(to='polls.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question_answers',
            field=models.ForeignKey(related_name='answers', to='polls.Question'),
            preserve_default=True,
        ),
    ]
