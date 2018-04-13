# Generated by Django 2.0.4 on 2018-04-12 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20180412_1249'),
    ]

    operations = [
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
            name='foto_produk',
            field=models.ImageField(blank=True, null=True, upload_to='foto'),
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