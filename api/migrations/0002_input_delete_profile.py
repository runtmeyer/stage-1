# Generated by Django 4.1.2 on 2022-11-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(choices=[('addition', 'add'), ('multiplication', 'multiply'), ('subtraction', 'minus')], max_length=20)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
