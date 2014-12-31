# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('cover', models.ImageField(upload_to=b'albums')),
                ('artist', models.ForeignKey(to='artists.Artist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
