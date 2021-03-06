# Generated by Django 3.2.9 on 2021-11-08 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_auto_20211107_0851'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='courses',
            name='lecture_question',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.coursecategory'),
        ),
    ]
