# Generated by Django 3.1.7 on 2021-04-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_auto_20210408_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='academic',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='depart',
            name='id',
        ),
        migrations.AlterField(
            model_name='depart',
            name='year',
            field=models.CharField(choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4t year')], max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
