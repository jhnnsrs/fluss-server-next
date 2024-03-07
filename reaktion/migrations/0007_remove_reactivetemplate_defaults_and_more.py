# Generated by Django 4.2.4 on 2023-09-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reaktion", "0006_rename_name_reactivetemplate_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reactivetemplate",
            name="defaults",
        ),
        migrations.AddConstraint(
            model_name="reactivetemplate",
            constraint=models.UniqueConstraint(
                fields=("title", "description"),
                name="Only one Reactive Template with this title and description",
            ),
        ),
    ]
