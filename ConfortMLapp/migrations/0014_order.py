# Generated by Django 4.2 on 2024-06-12 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ConfortMLapp', '0013_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=15)),
                ('customer_address', models.TextField()),
                ('payment_status', models.BooleanField(default=False)),
                ('invoice_pdf', models.FileField(blank=True, null=True, upload_to='invoices/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConfortMLapp.shop')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]