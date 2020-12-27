# Generated by Django 3.1.2 on 2020-12-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=600)),
                ('spotify_smug', models.CharField(max_length=30)),
                ('youtube_link', models.CharField(max_length=150)),
                ('podcast_image', models.ImageField(upload_to='podcasts/')),
            ],
        ),
    ]