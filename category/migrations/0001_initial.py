# Generated by Django 5.0.9 on 2024-09-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=80, unique=True)),
                ('slug', models.CharField(max_length=160, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cat_image', models.ImageField(blank=True, null=True, upload_to='photo/category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['category_name'],
            },
        ),
    ]
