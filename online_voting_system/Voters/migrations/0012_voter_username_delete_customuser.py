# Generated by Django 4.2.1 on 2023-05-20 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voters', '0011_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
