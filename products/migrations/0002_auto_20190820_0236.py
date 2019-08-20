# Generated by Django 2.2.4 on 2019-08-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('nalc', 'Non-Alcoholic'), ('liq', 'Liquor'), ('dbeer', 'Domestic Beer'), ('cbeer', 'Craft Beer'), ('pbeer', 'Premium Beer')], max_length=200),
        ),
    ]