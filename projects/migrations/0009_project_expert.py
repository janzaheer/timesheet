# Generated by Django 3.0.4 on 2020-04-11 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experts', '0003_auto_20200324_2039'),
        ('projects', '0008_auto_20200411_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expert_project', to='experts.Expert'),
        ),
    ]
