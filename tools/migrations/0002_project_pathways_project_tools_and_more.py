# Generated by Django 5.1.6 on 2025-03-18 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pathways',
            field=models.ManyToManyField(blank=True, related_name='projects', to='tools.pathway'),
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(blank=True, related_name='projects', to='tools.tool'),
        ),
        migrations.AlterField(
            model_name='horizonscan',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='horizon_scan', to='tools.project'),
        ),
        migrations.AlterField(
            model_name='pestle',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pestle', to='tools.project'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='pathways',
            field=models.ManyToManyField(blank=True, related_name='tools', to='tools.pathway'),
        ),
        migrations.DeleteModel(
            name='UserInput',
        ),
    ]
