# Generated by Django 3.0 on 2020-06-09 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ves', '0002_vagon_actnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagon',
            name='dateotgruzka',
            field=models.DateField(blank=True, null=True, verbose_name='дата отгнузки '),
        ),
        migrations.AddField(
            model_name='vagon',
            name='datepriem',
            field=models.DateField(blank=True, null=True, verbose_name='дата приемки '),
        ),
        migrations.AddField(
            model_name='vagon',
            name='datepriemsovmestny',
            field=models.DateField(blank=True, null=True, verbose_name='дата совместной приемки '),
        ),
    ]
