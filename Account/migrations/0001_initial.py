# Generated by Django 3.2.7 on 2021-09-20 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acc_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]