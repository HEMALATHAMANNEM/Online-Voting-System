# Generated by Django 4.2.1 on 2023-05-18 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Voters', '0003_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='password',
        ),
        migrations.AddField(
            model_name='candidate',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(null=True, upload_to='candidates'),
        ),
        migrations.AddField(
            model_name='voter',
            name='phone',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='voter',
            name='photo',
            field=models.ImageField(null=True, upload_to='voters'),
        ),
        migrations.AddField(
            model_name='voter',
            name='voted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='voter',
            name='email',
            field=models.EmailField(max_length=60, unique=True),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voters.candidate')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voters.position')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Voters.voter')),
            ],
        ),
    ]
