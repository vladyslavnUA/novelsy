# Generated by Django 3.0.3 on 2020-03-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200306_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(help_text='$', max_length=10),
        ),
    ]
