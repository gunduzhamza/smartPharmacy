# Generated by Django 4.0.3 on 2022-05-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0010_alter_recete_toplam'),
    ]

    operations = [
        migrations.AddField(
            model_name='recete',
            name='ilaclar',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='İlaçlar'),
        ),
    ]
