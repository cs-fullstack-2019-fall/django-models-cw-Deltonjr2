from django.db import models

# Exercise 1

# Add a new Dog model to your schema. Give it the fields: name, breed, color, and gender. Name should be a dog name, breed should be dog breed, color should be the color of the dog, and gender should be the gender of the dog.
#
# Using the admin site, create 3 dogs and save them in your database

class Dog(models.Model):
     Name= models.CharField(max_length=200,default="")
     Breed = models.CharField(max_length=100,default="")
     Color= models.IntegerField(default=0)
     Gender=models.CharField(max_length=200,default="")

# Exercise 2
# Add a new Account model to your schema. Give it the fields: username, realName, accountNumber, balance. Username should be a username the user uses to log in, the realName should be a user's real name, accountNumber should be the user's account number, and balance is the user's balance.
#
# Using the admin site, create 3 accounts and save them in your database.
class Dog(models.Model):
     UserName= models.CharField(max_length=200,default="")
     RealName = models.CharField(max_length=100,default="")
     AccountNumber= models.IntegerField(default=0)
     Balance=models.CharField(max_length=200,default=""