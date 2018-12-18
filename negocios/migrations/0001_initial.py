# Generated by Django 2.0.9 on 2018-12-18 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=25)),
                ('data_inicio', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15)),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotacoes', to='negocios.Acao')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='acao',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acoes', to='negocios.Empresa'),
        ),
    ]