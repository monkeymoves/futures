# Generated by Django 5.1.6 on 2025-03-13 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_alter_tool_description_alter_tool_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinput',
            name='input_data',
        ),
        migrations.CreateModel(
            name='HorizonScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horizon_scans', to='tools.project')),
            ],
        ),
        migrations.AddField(
            model_name='userinput',
            name='horizonscan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tools.horizonscan'),
        ),
        migrations.CreateModel(
            name='Pestle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('political', models.TextField(blank=True, null=True)),
                ('economic', models.TextField(blank=True, null=True)),
                ('social', models.TextField(blank=True, null=True)),
                ('technological', models.TextField(blank=True, null=True)),
                ('legal', models.TextField(blank=True, null=True)),
                ('environmental', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pestle_analyses', to='tools.project')),
            ],
        ),
        migrations.AddField(
            model_name='userinput',
            name='pestle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tools.pestle'),
        ),
    ]
