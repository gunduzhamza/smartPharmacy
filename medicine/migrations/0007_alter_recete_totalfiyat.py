# Generated by Django 4.0.3 on 2022-04-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0006_recete_totalfiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recete',
            name='totalfiyat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
