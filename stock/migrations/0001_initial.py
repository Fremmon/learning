# Generated by Django 3.2.8 on 2021-10-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('ticker', models.CharField(default='NULL', max_length=4)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
