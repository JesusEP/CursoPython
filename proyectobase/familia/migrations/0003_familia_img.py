# Generated by Django 4.0.4 on 2022-05-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0002_familia_alias_familia_born_alter_familia_kinship_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
