# Generated by Django 5.1.2 on 2024-10-25 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_intelectquest_intellect_quest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intelekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savol_matni', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Maxsus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savol_matni', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='intelectquest',
            name='intellect_quest',
        ),
        migrations.CreateModel(
            name='IntelektVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('savol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variantlar', to='main.intelekt')),
            ],
        ),
        migrations.CreateModel(
            name='MaxsusVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('savol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variantlar', to='main.maxsus')),
            ],
        ),
        migrations.DeleteModel(
            name='BasisQuests',
        ),
        migrations.DeleteModel(
            name='BasisQuestVariants',
        ),
        migrations.DeleteModel(
            name='IntelectQuest',
        ),
        migrations.DeleteModel(
            name='IntelectQuestVariant',
        ),
    ]
