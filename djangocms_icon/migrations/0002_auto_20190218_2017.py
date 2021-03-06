# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-18 20:17
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import F, Func, Value
from django.db.models.functions import Concat


def forwards_func(apps, schema_editor):
    icon = apps.get_model('djangocms_icon', 'Icon')

    icon.objects.filter(icon__startswith='el-icon-').update(icon=Concat(Value('el '), 'icon'))
    icon.objects.filter(icon__startswith='flag-icon-').update(icon=Concat(Value('flag-icon '), 'icon'))
    icon.objects.filter(icon__startswith='fa-').update(icon=Concat(Value('fa '), 'icon'))
    icon.objects.filter(icon__startswith='glyphicon-').update(icon=Concat(Value('glyphicon '), 'icon'))
    icon.objects.filter(icon__startswith='ion-').update(icon=Concat(Value('ion '), 'icon'))
    icon.objects.filter(icon__startswith='map-icon-').update(icon=Concat(Value('map-icon '), 'icon'))
    icon.objects.filter(icon__startswith='zmdi-').update(icon=Concat(Value('zmdi '), 'icon'))
    icon.objects.filter(icon__startswith='wi-').update(icon=Concat(Value('wi '), 'icon'))


def reverse_func(apps, schema_editor):
    icon = apps.get_model('djangocms_icon', 'Icon')

    icon.objects.filter(icon__startswith='el ').update(icon=Func(F('icon'), Value('el '), Value(''), function='replace',))
    icon.objects.filter(icon__startswith='flag-icon ').update(icon=Func(F('icon'), Value('flag-icon '), Value(''), function='replace',))
    icon.objects.filter(icon__startswith='fa ').update(icon=Func(F('icon'), Value('fa '), Value(''), function='replace',))
    icon.objects.filter(icon__startswith='glyphicon ').update(icon=Func(F('icon'), Value('glyphicon '), Value(''), function='replace',))
    icon.objects.filter(icon__startswith='map-icon ').update(icon=Func(F('icon'), Value('map-icon '), Value(''), function='replace',))
    icon.objects.filter(icon__startswith='zmdi ').update(icon=Func(F('icon'), Value('zmdi '), Value(''), function='replace',))
    icon.objects.filter(icon__startswith='wi ').update(icon=Func(F('icon'), Value('wi '), Value(''), function='replace',))


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_icon', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
