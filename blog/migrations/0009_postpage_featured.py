# Generated by Django 2.1.2 on 2018-11-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181030_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
