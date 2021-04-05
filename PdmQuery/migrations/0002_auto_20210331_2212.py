# Generated by Django 3.0.2 on 2021-03-31 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PdmQuery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icohm',
            name='Height_mm',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='icohm',
            name='PartNumber',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='icohm',
            name='Tolerance',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]