# Generated by Django 3.2.5 on 2021-07-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='tipo',
            field=models.CharField(default=1, max_length=100, verbose_name='Tipo Conta'),
            preserve_default=False,
        ),
    ]
