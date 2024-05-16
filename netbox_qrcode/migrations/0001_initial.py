# Generated by Django 5.0.6 on 2024-05-15 20:30

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0115_convert_dashboard_widgets'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRCodeSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('config', models.JSONField()),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('url', models.URLField(max_length=255)),
                ('assigned_object_id', models.PositiveBigIntegerField()),
                ('assigned_object_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(models.Q(('app_label', 'dcim'), ('model', 'cable')), models.Q(('app_label', 'dcim'), ('model', 'device')), models.Q(('app_label', 'dcim'), ('model', 'location')), models.Q(('app_label', 'dcim'), ('model', 'powerfeed')), models.Q(('app_label', 'dcim'), ('model', 'powerpanel')), models.Q(('app_label', 'dcim'), ('model', 'rack')), _connector='OR')), on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.contenttype')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'verbose_name': 'Custom URL',
                'verbose_name_plural': 'Custom URLs',
                'ordering': ('assigned_object_type', 'pk'),
                'indexes': [models.Index(fields=['assigned_object_type', 'assigned_object_id'], name='netbox_qrco_assigne_737197_idx')],
            },
        ),
    ]
