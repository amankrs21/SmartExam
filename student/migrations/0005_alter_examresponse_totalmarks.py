# Generated by Django 3.2.12 on 2022-09-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_examresponse_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examresponse',
            name='totalmarks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]