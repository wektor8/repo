# Generated by Django 2.2.12 on 2022-01-21 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20220121_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='proba',
            field=models.CharField(default='op', max_length=300),
            preserve_default=False,
        ),
    ]
