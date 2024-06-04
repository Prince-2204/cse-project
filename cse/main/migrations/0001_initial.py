# Generated by Django 4.2.11 on 2024-04-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('enrolment_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('exam_roll_no', models.IntegerField()),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.semester')),
                ('year_enrolled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.years')),
            ],
        ),
    ]