# Generated by Django 4.0.3 on 2022-03-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('steps', models.CharField(max_length=10000)),
                ('thumbnail', models.ImageField(default='', upload_to='posts/images')),
            ],
        ),
    ]