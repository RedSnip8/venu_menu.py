# Generated by Django 2.2.4 on 2019-08-20 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190820_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('nonalc', 'Non-Alcoholic'), ('liq', 'Liquor'), ('dombeer', 'Domestic Beer'), ('craftbeer', 'Craft Beer'), ('prembeer', 'Premium Beer')], max_length=200),
        ),
    ]
