#from statistics import mode
from django.db import models

class Voter(models.Model):
    firstname=models.CharField(max_length=25,null=True)
    lastname=models.CharField(max_length=25,null=True)
    username=models.CharField(max_length=50,null=True,unique=True)
    email=models.EmailField(max_length=60,null=True,unique=True)
    phone = models.IntegerField(null=True, unique=True)
    password=models.CharField(max_length=12,null=True)
    is_voted=models.BooleanField(default=False)
    #photo = models.ImageField(upload_to="voters",null=True)
    #voted = models.BooleanField(default=False)

    def __str__(self) :
        return self.firstname+" "+self.lastname
    
class Position(models.Model):
    name=models.CharField(max_length=25,null=True,unique=True)
    no_of_seats=models.IntegerField(default=1)
    def __str__(self) :
        return self.name

class Candidate(models.Model):
    firstname=models.CharField(max_length=25,null=True)
    lastname=models.CharField(max_length=25,null=True)
    username=models.CharField(max_length=25,null=True,unique=True)
    email=models.EmailField(max_length=60,null=True,unique=True)
    phone = models.IntegerField(null=True, unique=True)
    #photo = models.ImageField(upload_to="candidates",null=True)
    bio = models.TextField(null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,default="")
    no_of_votes = models.IntegerField(default=0)

    def __str__(self) :
        return self.firstname+" "+self.lastname

class Votes(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
