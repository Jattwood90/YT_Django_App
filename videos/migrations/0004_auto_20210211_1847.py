# Generated by Django 3.1.5 on 2021-02-11 18:47

from django.db import migrations, models
import django.db.models.deletion
import videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20210211_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yt',
            name='video',
            field=models.ForeignKey(default=videos.models.Video, null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.video'),
        ),
    ]
