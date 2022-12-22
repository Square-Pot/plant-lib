import os
from django.db import models
from django.contrib.auth.models import User


def get_avatar_filename(instance, filename):
    upload_to = 'avatars'
    ext = filename.split('.')[-1]
    filename = f"{instance.uid}.{ext}" 
    return os.path.join(upload_to, filename)


def create_uid(owner):
    no = Plant.objects.filter(owner=owner).count() + 1
    return f'{owner.id}|{no}'


class Plant(models.Model):
    uid = models.CharField(max_length=10, blank=True, editable=False) 
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False)

    # Dates
    date_created = models.DateTimeField(auto_now=True)
    date_purchase = models.DateTimeField(blank=True, null=True)
    deta_seeding = models.DateTimeField(blank=True, null=True)

    # Taxonomy fields
    genus = models.CharField(max_length=50, blank=False)
    species = models.CharField(max_length=50, blank=True)
    subspecies = models.CharField(max_length=50, blank=True)
    variety = models.CharField(max_length=50, blank=True)
    cultivar = models.CharField(max_length=50, blank=True)
    field_number = models.CharField(max_length=10, blank=True)
    form = models.CharField(max_length=50, blank=True)
    affinity = models.CharField(max_length=50, blank=True)
    ex = models.CharField(max_length=50, blank=True)

    # Additional info fields
    info = models.CharField(max_length=50, blank=True)
    geography = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    
    avatar = models.ImageField(upload_to=get_avatar_filename, blank=True)

    def save(self, *args, **kwargs):
        self.uid = create_uid(self.owner)
        super(Plant, self).save(*args, **kwargs)
        

    def __str__(self):
        return f"{self.uid} - {self.genus} {self.species}"