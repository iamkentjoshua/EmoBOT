# Generated by Django 3.1.4 on 2020-12-14 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emobot', '0004_auto_20201213_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default='2020-12-14'),
        ),
    ]