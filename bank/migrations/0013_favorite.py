# Generated by Django 2.1.3 on 2018-11-28 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20181128_0756'),
        ('bank', '0012_auto_20181128_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('name', models.CharField(default='', max_length=100)),
                ('bankaccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.BankAccount')),
            ],
        ),
    ]
