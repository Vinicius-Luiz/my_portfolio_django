# Generated by Django 4.2.1 on 2023-05-14 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_link_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='is_contact',
            field=models.BooleanField(default=False),
        ),
    ]
