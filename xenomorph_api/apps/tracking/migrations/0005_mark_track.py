# Generated by Django 4.1.2 on 2023-05-19 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tracking", "0004_remove_mark_track_alter_tracks_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="mark",
            name="track",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mark_track",
                to="tracking.tracks",
            ),
            preserve_default=False,
        ),
    ]
