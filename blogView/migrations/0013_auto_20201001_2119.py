# Generated by Django 3.0 on 2020-10-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogView', '0012_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Jay Prakash', max_length=50)),
                ('image', models.ImageField(upload_to='uploads/author')),
                ('words', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Anonymous', max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
