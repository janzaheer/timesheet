# Generated by Django 3.0.4 on 2020-03-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='identification_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='service_contract_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='sofreco_contract_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='timesheet',
            name='subject_of_contract',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]