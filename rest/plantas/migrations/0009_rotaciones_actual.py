# Generated by Django 2.2.4 on 2020-12-07 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plantas', '0008_tip_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotaciones',
            name='actual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actual', to='plantas.Familia'),
        ),
    ]
