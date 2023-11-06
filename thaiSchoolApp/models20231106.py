# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ExtData(models.Model):
    exttb_id = models.BigIntegerField(db_column='extTB_ID', blank=True, null=True)  # Field name made lowercase.
    school_id = models.ForeignKey('SchoolData', models.CASCADE , related_name='school_id', blank=True, null=True)
    room_s_6 = models.IntegerField(db_column='room_s.6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_p_4 = models.IntegerField(db_column='room_p.4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_k_3 = models.IntegerField(db_column='room_k.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_cert_2 = models.IntegerField(db_column='room_cert.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_s_4 = models.IntegerField(db_column='room_s.4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_p_6 = models.IntegerField(db_column='room_p.6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_p_3 = models.IntegerField(db_column='room_p.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_p_5 = models.IntegerField(db_column='room_p.5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_cert_3 = models.IntegerField(db_column='room_cert.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_s_5 = models.IntegerField(db_column='room_s.5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_s_2 = models.IntegerField(db_column='room_s.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    totalroom_field = models.IntegerField(db_column='totalroom_', blank=True, null=True)  # Field renamed because it ended with '_'.
    room_s_3 = models.IntegerField(db_column='room_s.3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_s_1 = models.IntegerField(db_column='room_s.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_k_2 = models.IntegerField(db_column='room_k.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_k_1 = models.IntegerField(db_column='room_k.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_cert_1 = models.IntegerField(db_column='room_cert.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_p_2 = models.IntegerField(db_column='room_p.2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    room_p_1 = models.IntegerField(db_column='room_p.1', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'ext_data'


class SchoolData(models.Model):
    school_id = models.TextField(primary_key=True)
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
        db_table = 'school_data'


class StudentData(models.Model):
    studenttb_id = models.BigIntegerField(db_column='studentTB_ID', blank=True, null=True)  # Field name made lowercase.
    school_id = models.ForeignKey(SchoolData, models.CASCADE ,related_name='school_id', blank=True, null=True)
    p_2_male = models.IntegerField(db_column='p.2_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_2_female = models.IntegerField(db_column='p.2_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_5_female = models.IntegerField(db_column='p.5_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_6_female = models.IntegerField(db_column='p.6_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_6_male = models.IntegerField(db_column='s.6_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_5_male = models.IntegerField(db_column='s.5_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_1_female = models.IntegerField(db_column='k.1_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cert_1_female = models.IntegerField(db_column='cert.1_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_6_female = models.IntegerField(db_column='s.6_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_4_male = models.IntegerField(db_column='p.4_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_4_male = models.IntegerField(db_column='s.4_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_3_male = models.IntegerField(db_column='s.3_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_6_male = models.IntegerField(db_column='p.6_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_2_female = models.IntegerField(db_column='s.2_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_1_male = models.IntegerField(db_column='k.1_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_2_male = models.IntegerField(db_column='k.2_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_2_male = models.IntegerField(db_column='s.2_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cert_1_male = models.IntegerField(db_column='cert.1_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_3_female = models.IntegerField(db_column='k.3_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_3_female = models.IntegerField(db_column='p.3_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_3_male = models.IntegerField(db_column='p.3_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_1_female = models.IntegerField(db_column='p.1_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_1_male = models.IntegerField(db_column='p.1_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cert_3_male = models.IntegerField(db_column='cert.3_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_3_male = models.IntegerField(db_column='k.3_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_5_female = models.IntegerField(db_column='s.5_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_3_female = models.IntegerField(db_column='s.3_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_1_male = models.IntegerField(db_column='s.1_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    k_2_female = models.IntegerField(db_column='k.2_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cert_2_female = models.IntegerField(db_column='cert.2_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_5_male = models.IntegerField(db_column='p.5_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_1_female = models.IntegerField(db_column='s.1_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    s_4_female = models.IntegerField(db_column='s.4_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    p_4_female = models.IntegerField(db_column='p.4_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cert_3_female = models.IntegerField(db_column='cert.3_female', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cert_2_male = models.IntegerField(db_column='cert.2_male', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'student_data'


class SummaryData(models.Model):
    summarytb_id = models.BigIntegerField(db_column='summaryTB_ID', blank=True, null=True)  # Field name made lowercase.
    school_id = models.ForeignKey(SchoolData, models.CASCADE,related_name='school_id', blank=True, null=True)
    pb_ext = models.TextField(blank=True, null=True)
    lowest_level = models.TextField(blank=True, null=True)
    highest_level = models.TextField(blank=True, null=True)
    total_p_field = models.IntegerField(db_column='total_p.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_s_upper = models.IntegerField(db_column='total_s._upper', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_k_field = models.IntegerField(db_column='total_k.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_s_lower = models.IntegerField(db_column='total_s._lower', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    total_studen = models.IntegerField(blank=True, null=True)
    total_cert_field = models.IntegerField(db_column='total_cert.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    size = models.TextField(blank=True, null=True)
    range = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'summary_data'
