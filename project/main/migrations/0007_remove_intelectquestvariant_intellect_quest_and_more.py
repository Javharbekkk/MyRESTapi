# Generated by Django 5.1.2 on 2024-10-24 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_intelectquest_remove_imsj_title_alter_imsj_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intelectquestvariant',
            name='intellect_quest',
        ),
        migrations.AddField(
            model_name='intelectquest',
            name='intellect_quest',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='main.intelectquestvariant'),
            preserve_default=False,
        ),
    ]
