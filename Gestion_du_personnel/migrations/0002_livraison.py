# Generated by Django 5.0.6 on 2024-06-23 16:28

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_du_personnel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('en cours', 'En cours'), ('livré', 'Livré')], max_length=100)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_du_personnel.employe')),
            ],
        ),
    ]