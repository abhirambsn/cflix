from django.db import models
import uuid

# Create your models here.

def get_filename(instance, filename):
    return 'uploads/music/{}.{}'.format(str(instance.id), filename.split('.')[1])

def get_up_path(instance, filename):
    return 'covers/music/{}.{}'.format(str(instance.id), filename.split('.')[1])

# Validators
# Music Validator

def get_extensions_for_type(general_type):
    import mimetypes
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext

def music_validator(value):
    import os, mimetypes
    from django.core.exceptions import ValidationError
    mimetypes.init()
    ext = value.name.split('.')[1]
    valid_extensions = tuple(get_extensions_for_type('audio'))
    if not '.{}'.format(ext.lower()) in valid_extensions:
        raise ValidationError("Invalid Audio File")

class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=60, blank=False, null=False)
    cover = models.ImageField(upload_to=get_up_path, blank=False, null=False)
    artist = models.CharField(max_length=40, blank=True, null=False)
    album = models.CharField(max_length=40, blank=True, null=False)
    file = models.FileField(upload_to=get_filename, validators=[music_validator], blank=False, null=False)