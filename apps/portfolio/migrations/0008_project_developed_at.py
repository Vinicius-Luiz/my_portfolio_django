# Generated by Django 4.2.1 on 2023-05-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_link_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='developed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
