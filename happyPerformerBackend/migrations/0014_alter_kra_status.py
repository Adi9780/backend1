
# Generated by Django 4.2.2 on 2025-02-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "happyPerformerBackend",
            "0013_rename_kpi_kra_kpi_rename_kra_kra_kra_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="kra",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Pending"), (1, "Approved"), (2, "Rejected")], default=0
            ),
        ),
    ]

# Generated by Django 4.2.2 on 2025-02-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "happyPerformerBackend",
            "0013_rename_kpi_kra_kpi_rename_kra_kra_kra_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="kra",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Pending"), (1, "Approved"), (2, "Rejected")], default=0
            ),
        ),
    ]

