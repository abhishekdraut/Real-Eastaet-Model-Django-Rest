# Generated by Django 3.2.9 on 2021-11-28 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NOI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rental_income', models.FloatField(blank=True, max_length=1000, null=True)),
                ('SF_month', models.FloatField(blank=True, max_length=100, null=True)),
                ('Total_noi', models.FloatField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Property_name', models.CharField(max_length=100)),
                ('Avg_unit_size', models.IntegerField()),
                ('units', models.IntegerField()),
                ('Gross_rent', models.FloatField(max_length=100)),
                ('Cap_rate', models.FloatField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Total_NOI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tota_NOI', models.FloatField(blank=True, max_length=1000, null=True)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='value.property')),
            ],
        ),
        migrations.CreateModel(
            name='Propert_Value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_value', models.FloatField(blank=True, max_length=1000, null=True)),
                ('NOI_calculations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='value.noi')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='value.property')),
            ],
        ),
        migrations.AddField(
            model_name='noi',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='value.property'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.FloatField(blank=True, max_length=1000, null=True)),
                ('insurance', models.FloatField(blank=True, max_length=1000, null=True)),
                ('Allowance', models.FloatField(blank=True, max_length=1000, null=True)),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='value.property')),
            ],
        ),
    ]
