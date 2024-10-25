# Generated by Django 5.1.2 on 2024-10-24 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_intelectquestvariant_intellect_quest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasisQuestVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('boolen', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BasisQuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('intellect_quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='main.basisquestvariant')),
            ],
        ),
    ]
