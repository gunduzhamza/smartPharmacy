# Generated by Django 4.0.3 on 2022-04-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_recete_qr_code_alter_medicine_ilacfiyati_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recete',
            name='totalfiyat',
            field=models.FloatField(blank=True, null=True),
        ),
    ]