# Generated by Django 5.1.6 on 2025-03-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_tool_project_alter_project_tools'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
