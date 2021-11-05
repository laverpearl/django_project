# Generated by Django 3.2.7 on 2021-10-27 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmark', '0002_alter_bookmark_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]