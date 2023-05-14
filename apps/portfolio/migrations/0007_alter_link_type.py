# Generated by Django 4.2.1 on 2023-05-14 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_aboutlink_about_alter_aboutlink_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='type',
            field=models.CharField(choices=[('LINKEDIN', 'LinkedIn'), ('GITHUB', 'GitHub'), ('KAGGLE', 'Kaggle'), ('CERTIFICATE', 'Certificado'), ('INSTAGRAM', 'Instagram'), ('OTHER', 'Outros')], max_length=128),
        ),
    ]