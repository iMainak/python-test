from django.db import models

# Create your models here.
class Sources(models.Model):
    id = models.IntegerField(db_column="id", primary_key=True)
    address = models.CharField(db_column="address", max_length=50, blank=True, null=True)
    business_Name  = models.CharField(db_column="business_Name", max_length=50, blank=True, null=True)
    person_Name = models.CharField(db_column="person_Name", max_length=50, blank=True, null=True)
    contact   = models.CharField(db_column="contact", max_length=50, blank=True, null=True)
    verified   = models.CharField(db_column="verified", max_length=50, blank=True, null=True)
    status   = models.CharField(db_column="status", max_length=50, blank=True, null=True)
    timeStamp  = models.CharField(db_column="timeStamp",  max_length=50, blank=True, null=True)
    class Meta:
        managed = False
        db_table = "sources"