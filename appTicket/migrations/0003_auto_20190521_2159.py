# Generated by Django 2.2.1 on 2019-05-22 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTicket', '0002_grupobandas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupobandas',
            name='estado',
            field=models.CharField(choices=[['Acre', 'Acre'], ['Amapá', 'Amapá'], ['Amazonas', 'Amazonas']], max_length=15),
        ),
    ]