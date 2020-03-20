# Generated by Django 3.0.3 on 2020-03-20 11:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20200319_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='accuracy',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='check_in',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='communication',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
