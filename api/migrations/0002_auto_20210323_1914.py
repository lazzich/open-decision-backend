# Generated by Django 3.1.3 on 2021-03-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='decisiontree',
            name='language',
            field=models.CharField(default='de_DE', max_length=200),
        ),
        migrations.AddField(
            model_name='decisiontree',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
