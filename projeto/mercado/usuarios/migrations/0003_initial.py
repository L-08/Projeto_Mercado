# Generated by Django 5.1.6 on 2025-06-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_Produto', models.CharField(max_length=45)),
                ('tipo', models.BooleanField()),
                ('preco', models.FloatField()),
                ('marca', models.CharField(max_length=25)),
            ],
        ),
    ]
