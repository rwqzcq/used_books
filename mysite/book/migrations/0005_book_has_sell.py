# Generated by Django 2.2.5 on 2020-02-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20200213_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='has_sell',
            field=models.IntegerField(default=0, verbose_name='已售数量'),
        ),
    ]