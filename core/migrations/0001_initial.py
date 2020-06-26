# Generated by Django 3.0.7 on 2020-06-25 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('unidade_medida', models.CharField(max_length=4)),
                ('qtde_estoque', models.DecimalField(decimal_places=4, max_digits=10)),
                ('valor_venda', models.DecimalField(decimal_places=4, max_digits=10)),
                ('qtde_reservada', models.DecimalField(decimal_places=4, max_digits=10)),
                ('qtde_disponivel', models.DecimalField(decimal_places=4, max_digits=10)),
                ('valor_custo', models.DecimalField(decimal_places=4, max_digits=10)),
                ('data_cadastro', models.DateTimeField(auto_now=True, verbose_name='Data de Cadastro')),
                ('data_desativacao', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField()),
                ('categoria', models.CharField(max_length=30)),
                ('tamanho', models.CharField(max_length=3)),
                ('cor', models.CharField(max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'produto',
            },
        ),
    ]
