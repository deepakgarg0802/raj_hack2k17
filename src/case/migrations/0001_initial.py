# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.7 on 2017-12-02 10:44
=======
# Generated by Django 1.11.7 on 2017-12-02 11:26
>>>>>>> af7b6ad69920d5c6bc7a47fa448359d0f5e75129
from __future__ import unicode_literals

import case.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('reg_from_loc', models.CharField(max_length=255)),
                ('ward_id', models.CharField(max_length=255)),
                ('incident_time', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Crime Categories',
            },
        ),
        migrations.CreateModel(
            name='CyberCaseCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Cyber Crime Categories',
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.FileField(upload_to=case.models.evidence_upload_location)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Witness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adhaar_id', models.CharField(max_length=20)),
                ('bahmashah_id', models.CharField(blank=True, max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='case.Case')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='case_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case.CaseCategory'),
        ),
        migrations.AddField(
            model_name='case',
            name='cyber_case_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case.CyberCaseCategories'),
        ),
    ]
