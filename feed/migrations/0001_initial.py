# Generated by Django 4.1.5 on 2023-01-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    # The model created in models.py is here stored in a DB schema with 'id' and 'text' columns
    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
            ],
        ),
    ]
