# Generated by Django 5.0.2 on 2024-05-20 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
