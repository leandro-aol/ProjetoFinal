# Generated by Django 2.1 on 2018-08-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
