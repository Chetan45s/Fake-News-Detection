# Generated by Django 2.1.1 on 2020-11-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_contribution'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputdata',
            name='result',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1')], max_length=50, null=True),
        ),
    ]