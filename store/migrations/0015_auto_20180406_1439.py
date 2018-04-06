# Generated by Django 2.0.3 on 2018-04-06 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20180406_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='id_kategori',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='keranjang_pembelian',
            name='id_pelanggan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pelanggan', to='store.Pelanggan'),
        ),
        migrations.AlterField(
            model_name='keranjang_pembelian',
            name='id_produk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produk', to='store.Produk'),
        ),
        migrations.AlterField(
            model_name='prediksi',
            name='id_rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Rating'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='kategori_produk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategori', to='store.Kategori'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id_pelanggan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Pelanggan'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id_produk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Produk'),
        ),
        migrations.AlterField(
            model_name='rekomendasi',
            name='id_pelanggan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Pelanggan'),
        ),
        migrations.AlterField(
            model_name='rekomendasi',
            name='id_prediksi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Prediksi'),
        ),
    ]