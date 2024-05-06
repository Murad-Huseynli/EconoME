# Generated by Django 3.2.14 on 2024-05-06 07:11

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(default='', max_length=50)),
                ('address', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=40), default=list, size=None)),
                ('logo', models.ImageField(upload_to='business/')),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('termsConditions', models.CharField(max_length=100)),
                ('startDate', models.DateField(null=True)),
                ('endDate', models.DateField(null=True)),
                ('isActive', models.BooleanField(default=False)),
                ('discountRateByGroup', models.JSONField(default={'': ''})),
                ('offeredBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deals.business')),
            ],
        ),
    ]
