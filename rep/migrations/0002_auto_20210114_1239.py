# Generated by Django 3.1.3 on 2021-01-14 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rep', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='meta_keywords',
            field=models.CharField(max_length=1000),
        ),
    ]
