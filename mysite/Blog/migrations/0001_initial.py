# Generated by Django 2.2.6 on 2019-11-08 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200, unique=True)),
                ('blog_slug', models.SlugField(max_length=200, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('blog_content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('blog_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]