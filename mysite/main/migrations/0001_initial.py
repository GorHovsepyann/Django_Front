# Generated by Django 5.0 on 2023-12-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Best_Jewellery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Hndik name')),
                ('button_name', models.CharField(max_length=50, verbose_name='Hndik button name')),
                ('about', models.TimeField(verbose_name='About hndik')),
                ('img', models.ImageField(upload_to='images', verbose_name='Hndik image')),
            ],
        ),
    ]