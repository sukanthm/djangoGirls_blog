# Generated by Django 2.2.3 on 2019-07-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='relevance',
            field=models.IntegerField(choices=[(1, 'important'), (2, 'trivial')], default=2),
        ),
    ]