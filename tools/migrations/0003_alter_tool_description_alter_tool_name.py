# Generated by Django 5.1.6 on 2025-03-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_project_userinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
