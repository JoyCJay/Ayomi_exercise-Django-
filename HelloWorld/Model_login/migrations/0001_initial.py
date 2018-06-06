# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('login', models.CharField(max_length=20)),
                ('mdp', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('mel', models.CharField(max_length=40)),
            ],
        ),
    ]
