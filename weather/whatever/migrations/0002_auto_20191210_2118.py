# Generated by Django 2.2.7 on 2019-12-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatever', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(max_length=1000),
        ),
    ]