# Generated by Django 4.0.3 on 2022-03-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_posts_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='media/posts/images'),
        ),
    ]
