# Generated by Django 2.1.5 on 2019-02-02 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.IntegerField(max_length=10)),
                ('file_name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('client_id', models.IntegerField(max_length=10)),
                ('date_uploaded', models.DateTimeField(verbose_name='date up')),
            ],
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_id', models.IntegerField(max_length=10)),
                ('portfolio_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='portfolioiamges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_id', models.IntegerField(max_length=10)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photography')),
                ('portfolio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.portfolio')),
            ],
        ),
        migrations.CreateModel(
            name='user_clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=16)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.photography')),
            ],
        ),
    ]
