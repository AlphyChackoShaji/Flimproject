# Generated by Django 3.2.16 on 2022-12-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='imgs',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]