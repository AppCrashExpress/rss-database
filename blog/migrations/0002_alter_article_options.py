# Generated by Django 3.2.4 on 2021-07-06 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('post_date',)},
        ),
    ]