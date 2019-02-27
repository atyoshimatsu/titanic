# Generated by Django 2.1.4 on 2019-01-01 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
                ('survived', models.BooleanField()),
                ('age', models.PositiveIntegerField(null=True)),
                ('ticket_class', models.PositiveSmallIntegerField()),
                ('embarked', models.CharField(choices=[('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')], max_length=1)),
            ],
        ),
    ]
