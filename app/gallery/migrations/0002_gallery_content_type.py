# Generated by Django 3.1.7 on 2021-04-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='content_type',
            field=models.CharField(default='image', max_length=50),
            preserve_default=False,
        ),
    ]