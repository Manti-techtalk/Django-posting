# Generated by Django 5.1.4 on 2024-12-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_posts_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
