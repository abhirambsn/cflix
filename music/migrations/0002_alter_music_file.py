# Generated by Django 3.2 on 2021-04-06 16:53

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='file',
            field=models.FileField(upload_to=music.models.get_filename, validators=[music.models.music_validator]),
        ),
    ]
