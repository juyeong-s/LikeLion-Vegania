# Generated by Django 3.2.4 on 2021-07-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0006_rename_agriculturalproducts_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='f5',
            field=models.TextField(default=1, verbose_name='면'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='f4',
            field=models.TextField(verbose_name='국'),
        ),
    ]
