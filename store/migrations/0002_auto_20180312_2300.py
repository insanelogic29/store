# Generated by Django 2.0.2 on 2018-03-12 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keranjang_pembelian',
            name='id_pelanggan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pelanggan', to='store.pelanggan'),
        ),
        migrations.AlterField(
            model_name='keranjang_pembelian',
            name='id_produk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produk', to='store.produk'),
        ),
    ]
