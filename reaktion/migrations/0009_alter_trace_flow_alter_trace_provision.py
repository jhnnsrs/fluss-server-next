# Generated by Django 4.2.4 on 2023-09-03 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("facade", "0007_node_defined_at_alter_provisionevent_provision"),
        ("reaktion", "0008_rename_kind_reactivetemplate_implementation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trace",
            name="flow",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="traces",
                to="reaktion.flow",
            ),
        ),
        migrations.AlterField(
            model_name="trace",
            name="provision",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="traces",
                to="facade.provision",
            ),
        ),
    ]
