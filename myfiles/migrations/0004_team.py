# Generated by Django 4.2.1 on 2023-05-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('lavozim', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('rasm', models.ImageField(upload_to='media')),
            ],
        ),
    ]
