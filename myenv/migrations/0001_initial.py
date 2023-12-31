# Generated by Django 4.2.6 on 2023-11-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('school_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('school_name', models.TextField(blank=True, null=True)),
                ('tel', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('branch', models.TextField(blank=True, null=True)),
                ('sector', models.TextField(blank=True, null=True)),
                ('subdistrict', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('county', models.TextField(blank=True, null=True)),
                ('group', models.TextField(blank=True, null=True)),
                ('village', models.TextField(blank=True, null=True)),
                ('post_office', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SummaryData',
            fields=[
                ('pb_ext', models.TextField(blank=True, null=True)),
                ('lowest_level', models.TextField(blank=True, null=True)),
                ('highest_level', models.TextField(blank=True, null=True)),
                ('total_s_upper', models.BigIntegerField(blank=True, db_column='total_s._upper', null=True)),
                ('total_cert_field', models.BigIntegerField(blank=True, db_column='total_cert.', null=True)),
                ('total_k_field', models.BigIntegerField(blank=True, db_column='total_k.', null=True)),
                ('total_p_field', models.BigIntegerField(blank=True, db_column='total_p.', null=True)),
                ('total_s_lower', models.BigIntegerField(blank=True, db_column='total_s._lower', null=True)),
                ('total_student', models.BigIntegerField(blank=True, null=True)),
                ('size', models.TextField(blank=True, null=True)),
                ('range', models.TextField(blank=True, null=True)),
                ('summarytb_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'summary_data',
                'managed': False,
            },
        ),
    ]
