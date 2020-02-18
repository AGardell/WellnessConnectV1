# Generated by Django 3.0.3 on 2020-02-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address_1', models.CharField(max_length=255)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': '"user"',
            },
        ),
    ]
