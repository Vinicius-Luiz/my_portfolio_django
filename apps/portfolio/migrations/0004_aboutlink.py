# Generated by Django 4.2.1 on 2023-05-14 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about', to='portfolio.about')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_links', to='portfolio.link')),
            ],
        ),
    ]
