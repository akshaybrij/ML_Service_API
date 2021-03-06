# Generated by Django 3.1 on 2020-11-28 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MLAlgorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=10000)),
                ('version', models.CharField(max_length=10)),
                ('owner', models.CharField(max_length=100)),
                ('created_at', models.CharField(max_length=100)),
                ('parent_endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.endpoint')),
            ],
        ),
        migrations.CreateModel(
            name='MLRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.CharField(max_length=10000)),
                ('full_response', models.TextField()),
                ('response', models.TextField()),
                ('feedback', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_mlalgorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.mlalgorithm')),
            ],
        ),
        migrations.CreateModel(
            name='MLAlgorithmStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=127)),
                ('active', models.BooleanField()),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parent_mlalgorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoints.mlalgorithm')),
            ],
        ),
    ]
