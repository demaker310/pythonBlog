# Generated by Django 3.1.3 on 2021-01-14 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rep', '0002_auto_20210114_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='meta_keywords',
            field=models.JSONField(verbose_name='keywords'),
        ),
    ]