# Generated by Django 3.0.7 on 2020-06-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='cod_gtin_ean',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='cod_origem',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(max_length=30, null=True),
        ),
    ]