# Generated by Django 2.1.1 on 2018-10-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('topic', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talker', models.CharField(max_length=10)),
                ('msg', models.TextField(max_length=64)),
            ],
        ),
    ]