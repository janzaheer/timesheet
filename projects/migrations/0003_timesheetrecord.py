# Generated by Django 3.0.4 on 2020-03-22 08:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200321_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheetRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('day', models.CharField(blank=True, choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thrusday', 'thrusday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], default='monday', max_length=200, null=True)),
                ('day_worked', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('nights_spent_in_cairo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('nights_spent_out_cairo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('place_of_activity', models.CharField(blank=True, max_length=200, null=True)),
                ('activities', models.CharField(blank=True, max_length=200, null=True)),
                ('total_month', models.CharField(blank=True, max_length=200, null=True)),
                ('timesheet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timesheet_record', to='projects.Timesheet')),
            ],
        ),
    ]