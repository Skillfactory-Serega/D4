# Generated by Django 4.0.4 on 2022-04-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(blank=True, through='news.PostCategory', to='news.category', verbose_name='Категория'),
        ),
    ]