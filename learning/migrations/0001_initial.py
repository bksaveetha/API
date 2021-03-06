# Generated by Django 3.1.7 on 2021-04-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic', models.IntegerField(choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4t year')])),
                ('courses', models.CharField(choices=[('HMT', 'Heat and Mass Transfer'), ('EE', 'English for Engineers'), ('RES', 'Renewable Energy Source'), ('SE', 'Software Engineers'), ('ST', 'Software Testing'), ('POM', 'Principle of management'), ('NT', 'Nano Technology'), ('MSWM', 'Municipal Solid Waste Management')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('mech', 'MECHANICAL'), ('cs', 'CS'), ('it', 'IT'), ('bio', 'biomedical'), ('eee', 'EEE'), ('civil', 'CIVIL')], max_length=6, unique=True)),
                ('year', models.IntegerField(choices=[('1', '1st year'), ('2', '2nd year'), ('3', '3rd year'), ('4', '4t year')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]
