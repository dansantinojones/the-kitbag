# Generated by Django 3.2 on 2023-03-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230319_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirt',
            name='image_url',
        ),
        migrations.AddField(
            model_name='shirt',
            name='size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]