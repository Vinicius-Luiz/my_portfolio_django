# Generated by Django 4.2.1 on 2023-05-14 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_project_developed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='developed_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
