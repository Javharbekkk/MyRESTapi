# Generated by Django 5.1.2 on 2024-10-24 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_imsj_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imsj',
            name='title',
            field=models.CharField(choices=[(1, 'Intelektual'), (2, 'Maxsus tayyorgarlik'), (3, 'Shaxsiy (ruhiy, psixologik)'), (4, 'Jismoniy')], max_length=255),
        ),
    ]
