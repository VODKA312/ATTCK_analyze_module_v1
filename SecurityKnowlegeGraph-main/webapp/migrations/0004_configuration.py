# Generated by Django 2.2.5 on 2022-11-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20221024_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('industry', models.CharField(max_length=256, verbose_name='行业')),
            ],
        ),
    ]