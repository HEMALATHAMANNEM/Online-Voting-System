# Generated by Django 4.2.1 on 2023-05-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voters', '0007_remove_candidate_photo_remove_voter_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='photo',
            field=models.ImageField(null=True, upload_to='voters'),
        ),
    ]
