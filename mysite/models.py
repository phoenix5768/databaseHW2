from django.db import models

# Create your models here.

class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField()

    def __str__(self):
        return self.cname

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

        managed = False
        db_table = 'country'


class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField()

    def __str__(self):
        return self.cname.cname + ' ' + self.disease_code.disease_code

    class Meta:
        verbose_name = 'Discover'
        verbose_name_plural = 'Discoveries'

        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)


class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey('Diseasetype', models.DO_NOTHING, db_column='id')

    def __str__(self):
        return self.disease_code

    class Meta:
        verbose_name = 'Disease'
        verbose_name_plural = 'Diseases'

        managed = False
        db_table = 'disease'


class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Disease Type'
        verbose_name_plural = 'Disease Types'

        managed = False
        db_table = 'diseasetype'


class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return self.email.email

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

        managed = False
        db_table = 'doctor'


class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.email.name

    class Meta:
        verbose_name = 'Public Servant'
        verbose_name_plural = 'Public Servants'

        managed = False
        db_table = 'publicservant'


class Record(models.Model):
    email = models.OneToOneField(Publicservant, models.DO_NOTHING, db_column='email', primary_key=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    def __str__(self):
        return self.email.email.email + ' ' + self.cname.cname

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)


class Specialize(models.Model):
    id = models.OneToOneField(Diseasetype, models.DO_NOTHING, db_column='id', primary_key=True)
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email')

    def __str__(self):
        return self.email.email.email

    class Meta:
        verbose_name = 'Specialize'
        verbose_name_plural = 'Specializes'

        managed = False
        db_table = 'specialize'
        unique_together = (('id', 'email'),)


class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        managed = False
        db_table = 'users'
