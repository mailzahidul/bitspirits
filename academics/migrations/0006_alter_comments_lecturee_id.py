# Generated by Django 3.2.9 on 2021-11-09 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_alter_courses_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='lecturee_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.lecturers'),
        ),
    ]