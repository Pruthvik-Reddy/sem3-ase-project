# Generated by Django 2.1.2 on 2018-11-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=30)),
                ('fees', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
