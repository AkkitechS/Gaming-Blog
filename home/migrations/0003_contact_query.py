# Generated by Django 4.0.3 on 2022-05-12 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='query',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
