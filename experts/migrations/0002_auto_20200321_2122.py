# Generated by Django 3.0.4 on 2020-03-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='expert',
            name='position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
