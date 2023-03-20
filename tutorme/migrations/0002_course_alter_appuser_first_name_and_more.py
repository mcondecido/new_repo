# Generated by Django 4.1.7 on 2023-03-20 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=10)),
                ('catalog_number', models.CharField(max_length=10)),
                ('course_id', models.CharField(max_length=10)),
                ('is_enrolled', models.BooleanField(default=False)),
                ('meeting_days', models.CharField(max_length=10)),
                ('start_time', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
