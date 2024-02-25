# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Country(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.name if self.name else ""


class Province(models.Model):
    name = models.CharField(max_length=255)
    country_id = models.ForeignKey(Country, db_column='country_id', null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'province'

    def __str__(self):
        return self.name if self.name else ""



class City(models.Model):
    name = models.CharField(max_length=255)
    province_id = models.ForeignKey(Province, db_column='province_id', null=True, on_delete=models.SET_NULL)
    # country_id = models.ForeignKey(Country, db_column='country_id', null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'city'

    def __str__(self):
        return self.name if self.name else ""