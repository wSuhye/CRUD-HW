# Generated by Django 2.2 on 2019-04-29 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='review',
            field=models.TextField(default='2'),
        ),
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.CharField(choices=[('1', '1점'), ('2', '2점'), ('3', '3점'), ('4', '4점'), ('5', '5점')], default='2', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]