# Generated by Django 3.1.6 on 2021-05-17 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pockethand',
            name='ranking',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
