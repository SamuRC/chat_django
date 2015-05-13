from django.db import models

# Create your models here.


class Room(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    status = models.CharField(max_length=2, default=0, null=True)

    class Meta:
        db_table = "rooms"


class User(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=2, default=1, null=True)
    last_login = models.BigIntegerField(null=True)
    creation_time = models.BigIntegerField(null=True)
    rooms = models.ManyToManyField(Room, db_table="users_rooms", verbose_name='Salas', blank=True)

    class Meta:
        db_table = "users"


class Client(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User)
    type = models.CharField(max_length=2, default=0, null=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "clients"


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    room = models.ForeignKey(Room)
    user = models.ForeignKey(User)
    text = models.CharField(max_length=400)
    creation_time = models.BigIntegerField(null=True)

    class Meta:
        db_table = "messages"


class Operator(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "operators"