# Generated by Django 3.0.8 on 2020-07-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogView', '0008_delete_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100)),
                ('bg_img', models.ImageField(upload_to='uploads/video')),
                ('pubDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
