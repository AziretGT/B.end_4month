# Generated by Django 4.1.7 on 2023-03-04 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_content_alter_post_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',), 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]