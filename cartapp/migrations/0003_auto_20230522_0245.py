# Generated by Django 3.2.16 on 2023-05-21 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_auto_20230521_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_a_quantity', models.PositiveIntegerField(default=0)),
                ('product_a_gift_wrap', models.BooleanField(default=False)),
                ('product_b_quantity', models.PositiveIntegerField(default=0)),
                ('product_b_gift_wrap', models.BooleanField(default=False)),
                ('product_c_quantity', models.PositiveIntegerField(default=0)),
                ('product_c_gift_wrap', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]