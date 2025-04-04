# Generated by Django 5.1.6 on 2025-03-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_merge_20250318_2057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='pathways',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pathways',
        ),
        migrations.RemoveField(
            model_name='pestle',
            name='project',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='description',
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(blank=True, to='tools.tool'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='HorizonScan',
        ),
        migrations.DeleteModel(
            name='Pathway',
        ),
        migrations.DeleteModel(
            name='Pestle',
        ),
    ]
