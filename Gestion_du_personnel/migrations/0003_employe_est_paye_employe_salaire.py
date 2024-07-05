# Generated by Django 5.0.6 on 2024-06-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_du_personnel', '0002_livraison'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='est_paye',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employe',
            name='salaire',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
