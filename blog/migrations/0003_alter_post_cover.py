# Generated by Django 4.2.1 on 2023-06-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_cover_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(upload_to='media/blog_covers'),
        ),
    ]
