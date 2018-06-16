from django.db import models
from django.contrib.auth.models import User
class Room(models.Model):
    name=models.CharField(max_length=128)
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Expense(models.Model):
    title=models.CharField(max_length=128)
    cost=models.BigIntegerField()
    date=models.DateTimeField()
    pay=models.BooleanField()
    buyer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='buyer')
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    users=models.ManyToManyField(User,related_name='users')
    def __str__(self):
        return self.title+'_'+str(self.room)+'_'+str(self.cost)

class Word(models.Model):
    text=models.CharField(max_length=1000)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Request(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner')
    type=models.PositiveSmallIntegerField()
    room=models.ForeignKey(Room,on_delete=models.CASCADE)

class RoomUser(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    permission=models.PositiveSmallIntegerField()