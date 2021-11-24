# Generated by Django 3.2.9 on 2021-11-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_usermodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='proficiency',
            field=models.CharField(choices=[('MASTER', 'MASTER'), ('PROFICIENT', 'PROFICIENT'), ('LEARNING', 'LEARNING'), ('LEARN IN FUTURE', 'LEARN IN FUTURE')], default='LEARNING', max_length=15),
        ),
    ]
