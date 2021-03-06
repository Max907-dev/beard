# Generated by Django 4.0.3 on 2022-04-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='created'),
        ),
        migrations.AlterField(
            model_name='images',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('deactivated', 'Deactivated')], default='active', max_length=11),
        ),
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
