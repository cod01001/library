# Generated by Django 5.0.1 on 2024-01-30 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_name_author_name_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(related_name='author', to='books.author'),
        ),
        migrations.AlterField(
            model_name='books',
            name='categories',
            field=models.ManyToManyField(related_name='category', to='books.category'),
        ),
    ]
