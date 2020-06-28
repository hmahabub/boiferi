# Generated by Django 3.0.7 on 2020-06-28 14:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='blog_post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('publish_date', models.DateField(blank=True, default=datetime.datetime(2020, 6, 28, 14, 26, 4, 812835, tzinfo=utc))),
            ],
            options={
                'get_latest_by': 'detail',
            },
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('borrow_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='profile_info',
            fields=[
                ('user', models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=10)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='book_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_category', models.CharField(max_length=100)),
                ('Author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handler.author')),
            ],
        ),
    ]
