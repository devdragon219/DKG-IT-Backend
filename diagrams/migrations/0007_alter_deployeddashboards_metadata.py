# Generated by Django 4.2 on 2024-07-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagrams', '0006_deployeddashboards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployeddashboards',
            name='metadata',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]