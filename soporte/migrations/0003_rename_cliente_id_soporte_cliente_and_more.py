# Generated by Django 4.2.3 on 2023-11-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soporte', '0002_alter_soporte_prioridad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='soporte',
            old_name='cliente_id',
            new_name='cliente',
        ),
        migrations.AlterField(
            model_name='soporte',
            name='estado',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='soporte',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='soporte',
            name='prioridad',
            field=models.CharField(max_length=10),
        ),
    ]
