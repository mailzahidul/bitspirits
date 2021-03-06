# Generated by Django 3.2.9 on 2021-11-06 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('image', models.ImageField(upload_to='lecturers/')),
                ('about', models.TextField()),
                ('qualification', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('linkdin', models.URLField(blank=True, null=True)),
                ('twetter', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('feature_img', models.ImageField(blank=True, null=True, upload_to='courses/')),
                ('fees', models.PositiveIntegerField()),
                ('featured', models.BooleanField(default=False)),
                ('duration', models.CharField(blank=True, max_length=20, null=True)),
                ('classes', models.CharField(blank=True, max_length=20, null=True)),
                ('time', models.CharField(blank=True, max_length=20, null=True)),
                ('lecture', models.CharField(blank=True, max_length=20, null=True)),
                ('lecture_question', models.CharField(blank=True, max_length=20, null=True)),
                ('lecture_description', models.TextField(blank=True, null=True)),
                ('lecture_duration', models.CharField(blank=True, max_length=20, null=True)),
                ('assigned_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.lecturers')),
            ],
        ),
    ]
