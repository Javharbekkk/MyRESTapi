# Generated by Django 5.1.2 on 2024-10-24 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_basisquest_intellect_quest_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BasisQuest',
            new_name='BasisQuests',
        ),
        migrations.RenameModel(
            old_name='BasisQuestVariant',
            new_name='BasisQuestVariants',
        ),
    ]
