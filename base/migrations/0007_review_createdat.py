# Generated by Django 3.2.6 on 2021-09-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
