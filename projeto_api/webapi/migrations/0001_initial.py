# Generated by Django 3.1 on 2020-08-28 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_nascimento', models.DateTimeField()),
            ],
        ),
    ]
