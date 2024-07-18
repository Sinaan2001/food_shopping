# Generated by Django 4.0.6 on 2024-06-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=250, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
