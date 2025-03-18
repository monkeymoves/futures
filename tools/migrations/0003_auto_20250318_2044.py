# tools/migrations/0002_auto_... (your file name will be different)
from django.db import migrations

def create_pathways_and_tools(apps, schema_editor):
    Pathway = apps.get_model('tools', 'Pathway')
    Tool = apps.get_model('tools', 'Tool')

    pathways_data = [
        {"name": "Building Futures intelligence", "description": "When scoping a future challenge"},
        {"name": "Creating a shared vision", "description": "Creating a shared vision of future success"},
        {"name": "Testing policy options with Futures scenarios under time constraints", "description": "Testing policy options with Futures scenarios under time constraints"},
        {"name": "Testing policy options with Futures scenarios", "description": "Testing policy options with Futures scenarios"},
        {"name": "Exploring dynamics of change", "description": "Exploring dynamics of change to understand alternative ways that policy might develop"},
        {"name": "Identifying gaps in your knowledge", "description": "Identifying gaps in your knowledge about what will be important in the future, in order to prioritise areas for further enquiry"},
        {"name": "Rigorous Futures process", "description": "Rigorous Futures process to inform strategic policy challenges"},
    ]

    tools_data = [
        {"name": "Delphi", "description": "A tool to help identify potential future trends"},
        {"name": "Seven Questions", "description": "A tool to help identify potential future trends"},
        {"name": "Horizon scanning", "description": "A tool to help identify potential future trends"},
        {"name": "Three Horizons", "description": "A tool to help identify potential future trends"},
        {"name": "Driver mapping", "description": "A tool to help identify potential future trends"},
        {"name": "SWOT", "description": "A tool to help identify potential future trends"},
        {"name": "Scenarios", "description": "A tool to help identify potential future trends"},
        {"name": "Visioning", "description": "A tool to help identify potential future trends"},
        {"name": "Futures Wheels", "description": "A tool to help identify potential future trends"},
        {"name": "Policy Stress-testing", "description": "A tool to help identify potential future trends"},
        {"name": "Roadmapping", "description": "A tool to help identify potential future trends"},
        {"name": "Backcasting", "description": "A tool to help identify potential future trends"},
        {"name": "PESTLE", "description": "A tool to help identify potential future trends"},
    ]

    for pathway_info in pathways_data:
        Pathway.objects.create(**pathway_info)

    for tool_info in tools_data:
        Tool.objects.create(**tool_info)

class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),  # Replace with the previous migration file name
    ]

    operations = [
        migrations.RunPython(create_pathways_and_tools),
    ]
