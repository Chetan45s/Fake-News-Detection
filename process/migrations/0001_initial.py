# Generated by Django 3.1.3 on 2020-11-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InputData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('result', models.CharField(blank=True, choices=[('0', '0'), ('1', '1')], max_length=50, null=True)),
            ],
        ),
    ]
