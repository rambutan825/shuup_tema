# Generated by Django 2.2.24 on 2021-07-22 14:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import shuup.core.fields


def ensure_allowed_next_statuses(apps, schema_editor):
    from shuup.core.models import OrderStatusManager

    # OrderStatus = apps.getModel("shuup", "OrderStatus")
    OrderStatusManager().ensure_allowed_next_statuses()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shuup", "0091_background_tasks"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderstatus",
            name="allowed_next_statuses",
            field=models.ManyToManyField(blank=True, to="shuup.OrderStatus", verbose_name="allowed next statuses"),
        ),
        migrations.AddField(
            model_name="orderstatus",
            name="visible_for_customer",
            field=models.BooleanField(
                default=True,
                help_text="Indicates whether this status is visible for the customers",
                verbose_name="is visible for the user",
            ),
        ),
        migrations.CreateModel(
            name="OrderStatusHistory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_on", models.DateTimeField(auto_now_add=True, verbose_name="created on")),
                ("description", models.TextField(blank=True, null=True, verbose_name="description")),
                (
                    "creator",
                    shuup.core.fields.UnsavedForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_status_history_created",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="creating user",
                    ),
                ),
                (
                    "next_order_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="next_order_status",
                        to="shuup.OrderStatus",
                        verbose_name="next order status",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="order_history",
                        to="shuup.Order",
                        verbose_name="order id",
                    ),
                ),
                (
                    "previous_order_status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="previous_order_status",
                        to="shuup.OrderStatus",
                        verbose_name="previous order status",
                    ),
                ),
            ],
        ),
        migrations.RunPython(ensure_allowed_next_statuses),
    ]
