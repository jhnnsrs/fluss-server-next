# Generated by Django 4.2.9 on 2024-07-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reaktion", "0002_alter_runevent_handle_alter_workspace_pinned_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="runevent",
            name="reference",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]