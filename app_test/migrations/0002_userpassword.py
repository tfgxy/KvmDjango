# Generated by Django 3.2.2 on 2021-05-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]