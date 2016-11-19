from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.  
class User(models.Model):
    p_id = models.AutoField(primary_key=True)
    id = models.TextField(blank=True, null=True)
    cardinality_csvlevel = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    consumerid = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    perishable_token = models.TextField(blank=True, null=True)
    cardinality_csv_session_token = models.TextField(blank=True, null=True)
    cardinality_csvregid = models.TextField(blank=True, null=True)
    cardinality_csvusername = models.TextField(blank=True, null=True)
    cardinality_csv_updated_at = models.TextField(blank=True, null=True)
    hashed_password = models.TextField(blank=True, null=True)
    referredfrom = models.TextField(blank=True, null=True)
    column_14 = models.IntegerField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = '_user'
#admin.site.register(User) 
class Userfinal(models.Model):
    p_id = models.AutoField(primary_key=True)
    id = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    consumerid = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    perishable_token = models.TextField(blank=True, null=True)
    session_token = models.TextField(blank=True, null=True)
    regid = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    totalreferalcount = models.TextField(blank=True, null=True)
    referalused = models.TextField(blank=True, null=True)

    column_12 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userfinal'



class Expenseparticipants(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.TextField(blank=True, null=True)
    share = models.DecimalField(max_digits=21, decimal_places=15, blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
#    field_id = models.TextField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    settled = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    participantname = models.TextField(blank=True, null=True)
    participant = models.TextField(blank=True, null=True)
    saved = models.IntegerField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    id1 = models.TextField(blank=True, null=True)

    comments = models.IntegerField(blank=True, null=True)

    column_14 = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
     return self.object
    class Meta:
        managed = False
        db_table = 'expenseparticipants'


class Expensedetails(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    id1 = models.TextField( blank=True, null=True)  # Field renamed because it started with '_'.
    description = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    addedby = models.TextField(blank=True, null=True)
    shares = models.TextField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    persons = models.TextField(blank=True, null=True)
    distribution = models.TextField(blank=True, null=True)
    owner = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    personsNames =  models.TextField(blank=True, null=True)
    sharesValues =  models.TextField(blank=True, null=True)
    expenseVersion =  models.TextField(blank=True, null=True)
    syncedString =  models.TextField(blank=True, null=True)
    deleted =  models.TextField(blank=True, null=True)

    column_17 = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
     return self.object
 
    class Meta:
        managed = False
        db_table = 'expensedetails'

class Runningexpenses(models.Model):
    p_id = models.AutoField(primary_key=True)
#    Expenseparticipants = models.ForeignKey(Expenseparticipants, unique=True)

    id = models.TextField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    saved = models.IntegerField(blank=True, null=True)
    agenda = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    contreemoney = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    field_created_at = models.IntegerField(db_column='_created_at', blank=True, null=True)  # Field renamed because it started with '_'.
    acl = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    id1 = models.TextField(db_column='id1', blank=True, null=True)  # Field renamed because it started with '_'.
    def __unicode__(self):
     return self.id1

    class Meta:
        managed = False
        db_table = 'runningexpenses'

  
class Updatelist(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    id1 = models.TextField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    dist = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    expenseid = models.TextField(blank=True, null=True)
    new_val = models.TextField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    old_val = models.TextField(blank=True, null=True)
    column_15 = models.IntegerField(blank=True, null=True)
#    p_id = models.AutoField()
    def __unicode__(self):
     return self.type


    class Meta:
        managed = False
        db_table = 'updatelist'
class Fcm(models.Model):
    instance_token = models.TextField(blank=True, null=True)
    p_id = models.AutoField(primary_key=True)
    def __unicode__(self):
     return self.instance_token

    class Meta:
        managed = False
        db_table = 'FCM'

class Merchantofferings(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.TextField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    itemslist = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    merchantname = models.TextField(blank=True, null=True)
    available = models.TextField(blank=True, null=True)
    itemprice = models.TextField(blank=True, null=True)
    merchantnumber = models.TextField(blank=True, null=True)
    conveniencefee = models.TextField(blank=True, null=True)
    netamount = models.IntegerField(blank=True, null=True)
    settledamount = models.IntegerField(blank=True, null=True)
    column_16 = models.IntegerField(blank=True, null=True)
#    p_id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'merchantofferings'
class Referral(models.Model):
    p_id = models.AutoField(primary_key=True)

    id = models.TextField(blank=True, null=True)
    referralcount = models.IntegerField(blank=True, null=True)
    rperm = models.TextField(blank=True, null=True)
    referralcode = models.TextField(blank=True, null=True)
    acl = models.TextField(blank=True, null=True)
    wperm = models.TextField(blank=True, null=True)
    created_at = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    updated_at = models.TextField(blank=True, null=True)
    column_10 = models.TextField(blank=True, null=True)
    totalreferalcount = models.TextField(blank=True, null=True)
    referalused = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral'
class Userorder(models.Model):
    p_id = models.AutoField(primary_key=True)

    eta = models.CharField(max_length=11, blank=True, null=True)
    amountitems = models.CharField(max_length=5, blank=True, null=True)
    available = models.CharField(max_length=5, blank=True, null=True)
    category = models.CharField(max_length=6, blank=True, null=True)
    confreestatus = models.CharField(max_length=2, blank=True, null=True)
    createdat = models.CharField(max_length=24, blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    itemprice = models.CharField(max_length=8, blank=True, null=True)
    itemslist = models.CharField(max_length=34, blank=True, null=True)
    merchantname = models.CharField(max_length=11, blank=True, null=True)
    merchantnumber = models.TextField(blank=True, null=True)
    netprice = models.IntegerField(blank=True, null=True)
    objectid = models.CharField(max_length=10, blank=True, null=True)
    orderid = models.CharField(max_length=24, blank=True, null=True)
    orderno = models.CharField(max_length=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updatedat = models.CharField(max_length=24, blank=True, null=True)
    username = models.CharField(max_length=9, blank=True, null=True)
    usernumber = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userorder'

