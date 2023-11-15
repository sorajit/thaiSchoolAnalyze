# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SchoolData(models.Model):
    school_id = models.BigIntegerField(primary_key=True)
    school_name = models.TextField(blank=True, null=True)
    tel = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    branch = models.TextField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    subdistrict = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    group = models.TextField(blank=True, null=True)
    village = models.TextField(blank=True, null=True)
    post_office = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_data'


class SummaryData(models.Model):
    school = models.ForeignKey(SchoolData, models.DO_NOTHING, blank=True, null=True)
    pb_ext = models.TextField(blank=True, null=True)
    lowest_level = models.TextField(blank=True, null=True)
    highest_level = models.TextField(blank=True, null=True)
    total_s_upper = models.BigIntegerField(db_column='total_s._upper', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_cert_field = models.BigIntegerField(db_column='total_cert.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_k_field = models.BigIntegerField(db_column='total_k.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_p_field = models.BigIntegerField(db_column='total_p.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_s_lower = models.BigIntegerField(db_column='total_s._lower', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_student = models.BigIntegerField(blank=True, null=True)
    size = models.TextField(blank=True, null=True)
    range = models.TextField(blank=True, null=True)
    summarytb_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'summary_data'
