# Generated by Django 3.0.3 on 2020-06-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200317_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='decisiontree',
            name='extra_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='decisiontree',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]
