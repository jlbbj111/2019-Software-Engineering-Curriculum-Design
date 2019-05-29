# Generated by Django 2.1.7 on 2019-05-29 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backstage', '0001_initial'),
        ('courseScheduling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('commen_score', models.FloatField(default=0)),
                ('final_score', models.FloatField(default=0)),
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Student')),
                ('teaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseScheduling.Teaching')),
            ],
            options={
                'db_table': 'course_score',
            },
        ),
        migrations.CreateModel(
            name='EvaluationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.IntegerField(default=0)),
                ('item2', models.IntegerField(default=0)),
                ('item3', models.IntegerField(default=0)),
                ('item4', models.IntegerField(default=0)),
                ('item5', models.IntegerField(default=0)),
                ('item6', models.IntegerField(default=0)),
                ('item7', models.IntegerField(default=0)),
                ('item8', models.IntegerField(default=0)),
                ('description', models.TextField(default='无')),
                ('sum', models.FloatField(default=0)),
                ('is_finish', models.BooleanField(default=False)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='courseScheduling.MajorCourses')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backstage.Student')),
                ('teacher', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backstage.Teacher')),
            ],
            options={
                'db_table': 'evaluation_form',
            },
        ),
        migrations.AlterUniqueTogether(
            name='coursescore',
            unique_together={('teaching', 'sno')},
        ),
    ]
