# Generated by Django 3.2.6 on 2021-08-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='content',
            field=models.TextField(default='ab'),
        ),
    ]