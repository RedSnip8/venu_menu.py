# Generated by Django 2.2.4 on 2019-08-20 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('stands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Product')),
                ('stand_code_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stands.Stand')),
            ],
        ),
    ]
