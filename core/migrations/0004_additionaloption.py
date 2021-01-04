# Generated by Django 2.1.15 on 2021-01-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210104_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=250, null=True)),
                ('optionname', models.CharField(blank=True, max_length=250, null=True)),
                ('optionvalue', models.FloatField(blank=True, null=True)),
                ('markuprate', models.IntegerField(blank=True, default=35, null=True, verbose_name='Mark-Up Rate')),
            ],
            options={
                'verbose_name': 'Additional Options',
                'verbose_name_plural': 'Additionals Options',
                'db_table': 'tbl_additionaloption',
                'managed': True,
            },
        ),
    ]
