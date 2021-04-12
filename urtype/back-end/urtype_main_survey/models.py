from django.db import models

class Globals(models.Model):
    brand_Name = models.CharField(db_column='brand_Name', primary_key=True, max_length=100)  # Field name made lowercase.
    brand_Ment = models.CharField(db_column='brand_Ment', max_length=500)  # Field name made lowercase.
    brand_Genre = models.CharField(db_column='brand_Genre', max_length=45)  # Field name made lowercase.
    design_Point = models.CharField(db_column='design_Point', max_length=10)  # Field name made lowercase.
    design_Color = models.CharField(db_column='design_Color', max_length=10)  # Field name made lowercase.
    avg_Price = models.CharField(db_column='avg_Price', max_length=10)  # Field name made lowercase.
    brand_Url = models.CharField(db_column='brand_Url', max_length=100)  # Field name made lowercase.
    brand_Img = models.CharField(db_column='brand_Img', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'globals'


class Middle(models.Model):
    brand_Name = models.CharField(db_column='brand_Name', primary_key=True, max_length=100)  # Field name made lowercase.
    brand_Ment = models.CharField(db_column='brand_Ment', max_length=500)  # Field name made lowercase.
    brand_Genre = models.CharField(db_column='brand_Genre', max_length=45)  # Field name made lowercase.
    design_Point = models.CharField(db_column='design_Point', max_length=10)  # Field name made lowercase.
    design_Color = models.CharField(db_column='design_Color', max_length=10)  # Field name made lowercase.
    avg_Price = models.CharField(db_column='avg_Price', max_length=10)  # Field name made lowercase.
    brand_Url = models.CharField(db_column='brand_Url', max_length=100)  # Field name made lowercase.
    brand_Img = models.CharField(db_column='brand_Img', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'middle'


class National(models.Model):
    brand_Name = models.CharField(db_column='brand_Name', primary_key=True, max_length=100)  # Field name made lowercase.
    brand_Ment = models.CharField(db_column='brand_Ment', max_length=500)  # Field name made lowercase.
    brand_Genre = models.CharField(db_column='brand_Genre', max_length=45)  # Field name made lowercase.
    design_Point = models.CharField(db_column='design_Point', max_length=10)  # Field name made lowercase.
    design_Color = models.CharField(db_column='design_Color', max_length=10)  # Field name made lowercase.
    avg_Price = models.CharField(db_column='avg_Price', max_length=10)  # Field name made lowercase.
    brand_Url = models.CharField(db_column='brand_Url', max_length=100)  # Field name made lowercase.
    brand_Img = models.CharField(db_column='brand_Img', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'national'


class Soho(models.Model):
    brand_Name = models.CharField(db_column='brand_Name', primary_key=True, max_length=100)  # Field name made lowercase.
    brand_Ment = models.CharField(db_column='brand_Ment', max_length=500)  # Field name made lowercase.
    brand_Genre = models.CharField(db_column='brand_Genre', max_length=45)  # Field name made lowercase.
    design_Point = models.CharField(db_column='design_Point', max_length=10)  # Field name made lowercase.
    design_Color = models.CharField(db_column='design_Color', max_length=10)  # Field name made lowercase.
    avg_Price = models.CharField(db_column='avg_Price', max_length=10)  # Field name made lowercase.
    brand_Url = models.CharField(db_column='brand_Url', max_length=100)  # Field name made lowercase.
    brand_Img = models.CharField(db_column='brand_Img', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soho'


class Userinfo(models.Model):
    user_id = models.AutoField(db_column='user_ID', primary_key=True)  # Field name made lowercase.
    user_age = models.CharField(db_column='user_Age', max_length=45)  # Field name made lowercase.
    user_job = models.CharField(db_column='user_Job', max_length=20)  # Field name made lowercase.
    brand_name = models.CharField(db_column='brand_Name', max_length=150)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userInfo'