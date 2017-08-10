# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '__first__'),
        ('artists', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('order', models.PositiveIntegerField()),
                ('track_file', models.FileField(upload_to=b'tracks')),
                ('album', models.ForeignKey(to='albums.Album')),
                ('artist', models.ForeignKey(to='artists.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
