# Generated by Django 2.1.1 on 2018-12-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181230_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogcontent',
            field=models.TextField(max_length=50000, null=True),
        ),
    ]
