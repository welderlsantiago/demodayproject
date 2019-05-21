# Generated by Django 2.2.1 on 2019-05-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTicket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoBandas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('estado', models.CharField(choices=[['acre', 'Acre'], ['amapa', 'Amapá'], ['amazonas', 'Amazonas']], max_length=15)),
                ('biografia', models.CharField(max_length=300)),
                ('foto', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
