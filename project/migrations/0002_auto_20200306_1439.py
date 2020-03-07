# Generated by Django 3.0.3 on 2020-03-06 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='content',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created',
        ),
        migrations.RemoveField(
            model_name='book',
            name='modified',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(default='', help_text='Author of the book', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='', help_text='Write the description of your Book here.'),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.TextField(default='sample_link', help_text='link to picture of book'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default='$5.00', help_text='How much will this book cost?'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text='The user that listed this book.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.CharField(blank=True, editable=False, help_text='Unique URL path to access this Book. Generated by the system.', max_length=250),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Title of your Book.', max_length=250, unique=True),
        ),
    ]
