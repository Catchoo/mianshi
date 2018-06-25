# Generated by Django 2.0 on 2018-06-23 09:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('download_excel', '0002_auto_20180623_0934'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='orgnz',
            name='type_idx',
        ),
        migrations.AlterField(
            model_name='people',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ab9a452b-eb53-4dbf-afb2-d853744d3440'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='orgnz',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddIndex(
            model_name='people',
            index=models.Index(fields=['ID'], name='ID_idx'),
        ),
    ]