# Generated by Django 3.2 on 2023-03-27 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboardapp', '0002_auto_20230324_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='status',
            field=models.CharField(choices=[('Go', 'Хорошее'), ('No', 'Среднее'), ('Bad', 'Плохое')], default='Go', max_length=50),
        ),
    ]
