# Generated by Django 3.2.12 on 2022-03-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0003_stu_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='stu',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
