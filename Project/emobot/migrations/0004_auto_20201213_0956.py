# Generated by Django 3.1.4 on 2020-12-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emobot', '0003_auto_20201212_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='email',
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(default='2020-12-13'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
