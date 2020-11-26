# Generated by Django 2.2.16 on 2020-11-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0078_set_null_product_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributelogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='attributelogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='carrierlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='carrierlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='categorylogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='categorylogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='companycontactlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='companycontactlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='contactgrouplogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='contactgrouplogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='currencylogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='currencylogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='customertaxgrouplogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='customertaxgrouplogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='manufacturerlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='manufacturerlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='orderlinelogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='orderlinelogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='orderlinetaxlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='orderlinetaxlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='orderlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='orderlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='paymentlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='paymentlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='paymentmethodlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='paymentmethodlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='paymentprocessorlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='paymentprocessorlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='personcontactlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='personcontactlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='productlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='productlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='productmedialogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='productmedialogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='savedaddresslogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='savedaddresslogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='shipmentlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='shipmentlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='shipmentproductlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='shipmentproductlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='shippingmethodlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='shippingmethodlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='shoplogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='shoplogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='shopproductlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='shopproductlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='suppliedproductlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='suppliedproductlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='supplierlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='supplierlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='taxclasslogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='taxclasslogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='taxlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='taxlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
    ]
