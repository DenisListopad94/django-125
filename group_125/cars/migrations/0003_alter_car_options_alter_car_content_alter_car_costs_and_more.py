# Generated by Django 4.0.4 on 2022-04-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Мaшины', 'verbose_name_plural': 'машины'},
        ),
        migrations.AlterField(
            model_name='car',
            name='content',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='car',
            name='costs',
            field=models.IntegerField(verbose_name='стоимость'),
        ),
        migrations.AlterField(
            model_name='car',
            name='create',
            field=models.IntegerField(default=2010, verbose_name='дата выпуска'),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=40, verbose_name='машины'),
        ),
    ]
