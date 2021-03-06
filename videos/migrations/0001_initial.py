# Generated by Django 3.1.7 on 2021-04-06 05:17

from django.db import migrations, models
import uuid
import videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('cover', models.ImageField(upload_to=videos.models.get_up_path)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to=videos.models.get_filename)),
            ],
        ),
    ]
