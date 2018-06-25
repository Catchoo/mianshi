# Generated by Django 2.0 on 2018-06-23 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('download_excel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='orgnz',
            name='type_idx',
        ),
        migrations.AlterField(
            model_name='people',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('8cdac5bf-49b5-4e6d-9fd2-5f1fa7e12958'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddIndex(
            model_name='orgnz',
            index=models.Index(fields=['name'], name='type_idx'),
        ),
    ]