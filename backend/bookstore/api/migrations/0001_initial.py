# Generated by Django 5.1 on 2024-08-20 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Mystery', 'Mystery'), ('Thriller', 'Thriller'), ('Sci-Fi', 'Sci-Fi'), ('Humor', 'Humor'), ('Horror', 'Horror')], max_length=30)),
                ('first_pub', models.DateTimeField(auto_now_add=True)),
                ('last_pub', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
