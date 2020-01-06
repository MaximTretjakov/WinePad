# Generated by Django 3.0.2 on 2020-01-03 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrative_area', models.CharField(max_length=100, verbose_name='administrative_area')),
            ],
            options={
                'verbose_name': 'administrative area',
                'verbose_name_plural': 'administrative area',
                'ordering': ('administrative_area',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
                'ordering': ('country',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100, verbose_name='region')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depend_form.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
                'ordering': ('region',),
            },
        ),
        migrations.CreateModel(
            name='QualityMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality_mark', models.CharField(max_length=100, verbose_name='quality_mark')),
                ('administrative_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depend_form.AdministrativeArea', verbose_name='administrative_area')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depend_form.Country', verbose_name='country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depend_form.Region', verbose_name='region')),
            ],
            options={
                'verbose_name': 'quality mark',
                'verbose_name_plural': 'quality mark',
                'ordering': ('quality_mark',),
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vine', models.CharField(max_length=100, verbose_name='vine')),
                ('quality_mark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depend_form.QualityMark', verbose_name='quality_mark')),
            ],
            options={
                'verbose_name': 'container',
            },
        ),
        migrations.AddField(
            model_name='administrativearea',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='depend_form.Region', verbose_name='region'),
        ),
    ]
