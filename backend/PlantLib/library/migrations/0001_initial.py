# Generated by Django 4.1.4 on 2022-12-22 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=7, unique=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_purchase', models.DateTimeField(blank=True)),
                ('deta_seeding', models.DateTimeField(blank=True)),
                ('genus', models.CharField(max_length=50)),
                ('species', models.CharField(blank=True, max_length=50)),
                ('subspecies', models.CharField(blank=True, max_length=50)),
                ('variety', models.CharField(blank=True, max_length=50)),
                ('cultivar', models.CharField(blank=True, max_length=50)),
                ('field_number', models.CharField(blank=True, max_length=10)),
                ('form', models.CharField(blank=True, max_length=50)),
                ('affinity', models.CharField(blank=True, max_length=50)),
                ('ex', models.CharField(blank=True, max_length=50)),
                ('info', models.CharField(blank=True, max_length=50)),
                ('geography', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(blank=True, max_length=50)),
                ('price', models.CharField(blank=True, max_length=10)),
                ('description', models.TextField()),
                ('avatar', models.ImageField(upload_to=library.models.get_avatar_filename)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
