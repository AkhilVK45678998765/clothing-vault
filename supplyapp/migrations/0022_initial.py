# Generated by Django 4.1.7 on 2023-05-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplyapp', '0021_delete_buymodel_delete_cartmodel_delete_feedmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='buymodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('paymode', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='cartmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='feedmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='logmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='shoplogmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='shopregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='wishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('image', models.FileField(upload_to='supplyapp/static')),
            ],
        ),
    ]
