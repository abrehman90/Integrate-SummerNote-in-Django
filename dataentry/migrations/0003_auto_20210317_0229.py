# Generated by Django 3.1.7 on 2021-03-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='+92', max_length=25),
        ),
    ]