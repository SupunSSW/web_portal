# Generated by Django 3.0.5 on 2020-04-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uindex', models.CharField(max_length=30)),
                ('imgname', models.CharField(max_length=100)),
            ],
        ),
    ]
