# Generated by Django 2.1.3 on 2018-11-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_auto_20181128_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionlog',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
