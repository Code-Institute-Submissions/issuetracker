# Generated by Django 2.0.2 on 2018-02-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('features1', models.TextField()),
                ('features2', models.TextField()),
                ('features3', models.TextField()),
                ('features4', models.TextField()),
            ],
        ),
    ]