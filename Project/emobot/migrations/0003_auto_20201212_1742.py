# Generated by Django 3.1.4 on 2020-12-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emobot', '0002_auto_20201212_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
