# Generated by Django 2.2 on 2022-03-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_avodha_app', '0002_shop_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
