# Generated by Django 5.1.2 on 2024-10-24 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_imsj_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imsj',
            name='title',
            field=models.CharField(choices=[(2, 'Intelektual'), (1, 'Maxsus tayyorgarlik'), (4, 'Shaxsiy (ruhiy, psixologik)'), (3, 'Jismoniy')], max_length=255),
        ),
    ]