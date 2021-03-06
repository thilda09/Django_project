# Generated by Django 2.0 on 2018-01-08 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billetage',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
                ('type', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('premon', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Creance',
            fields=[
                ('id', models.IntegerField(max_length=11, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Versement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banque', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('type_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='zooma.Type')),
                ('type', models.CharField(max_length=11)),
            ],
            bases=('zooma.type',),
        ),
    ]
