# Generated by Django 3.2.9 on 2021-11-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insti_name', models.CharField(max_length=100)),
                ('insti_logo', models.ImageField(blank=True, null=True, upload_to='institute/')),
                ('insti_description', models.TextField(blank=True, null=True)),
                ('insti_phone', models.CharField(blank=True, max_length=11, null=True)),
                ('insti_address', models.CharField(max_length=11)),
                ('insti_email', models.EmailField(max_length=254)),
                ('insti_facebook', models.URLField(blank=True, null=True)),
                ('insti_twitter', models.URLField(blank=True, null=True)),
                ('insti_linkdin', models.URLField(blank=True, null=True)),
                ('insti_pinterest', models.URLField(blank=True, null=True)),
            ],
        ),
    ]